import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import json
import pystac

def read_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return json

class FileCreatedHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return None

        if event.event_type == 'created':
            # The file has been created, you can now process it
            file_path = event.src_path
            filename = os.path.basename(file_path)
            print(f"New file created: {filename}")
            if os.path.split(filename)[-1] == 'json':
                self.process_file(file_path)

    def process_file(self, file_path):
        print(f"Processing: {filename} ...")
        data = read_json(filename)
    
    def create_item(self, data):
        item = pystac.Item(

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
