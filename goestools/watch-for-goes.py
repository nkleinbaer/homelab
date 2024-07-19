import time
from datetime import datetime as Datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import requests
import os
import json
import pystac
from pathlib import Path
import re
from shapely.geometry import Polygon, mapping


def read_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data 

class FileCreatedHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return None

        if event.event_type == 'created':
            # The file has been created, you can now process it
            file_path = Path(event.src_path)
            print(f"New file created: {file_path}")
            extension = file_path.suffix
            if extension == '.json':
                self.process_file(file_path)

    def process_file(self, file_path):
        print(f"Processing: {file_path} ...")
        data = read_json(file_path)
        self.create_item(data)
 
    def create_item(self, data):
        annotation = data.get("Annotation")
        split = annotation.split('_') 
        id = f'{split[0]}_{split[1][:-6]}_{split[2]}_{split[3]}'
        bbox = [-156.268032341, -81.317211843, 6.133820020999991, 81.32434805]
        geometry =  mapping(Polygon( 
                    [
                                    [-156.268032341, -81.317211843],
                                    [-156.268032341, 81.32434805],
                                    [6.133820020999991, 81.32434805],
                                    [6.133820020999991, -81.317211843],
                                    [-156.268032341, -81.317211843]
                    ]
        ))
                        
        datetime = Datetime.fromisoformat(data.get("TimeStamp").get("ISO8601"))
        item = pystac.Item(id=id, geometry=geometry,bbox=bbox, datetime=datetime, properties={}, collection='goes16-fd')
        path = data.get("Path")
        asset = pystac.Asset(href=path)
        channel = data.get("AncillaryText").get("Channel")
        item.add_asset(key=channel, asset=asset)
        self.write_item(item)

    def write_item(self, item):
        print(json.dumps(item.to_dict()))
        resp = requests.post("http://192.168.1.237:8082/collections/goes16-fd/items", json=item.to_dict())
        print(resp.content)

if __name__ == "__main__":
    path = "/mnt/data/goes"  # Replace with your shared volume path
    event_handler = FileCreatedHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
