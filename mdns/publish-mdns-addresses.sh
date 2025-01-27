#!/bin/bash

function _term {
  pkill -P $$
}

trap _term SIGTERM

/usr/bin/avahi-publish -a grafana.local -R 192.168.1.243 &
/usr/bin/avahi-publish -a plane.local -R 192.168.1.243 &
/usr/bin/avahi-publish -a plane-minio.local -R 192.168.1.243 &
/usr/bin/avahi-publish -a traefik.local -R 192.168.1.243 &

while true; do sleep 10000; done
