#!/bin/sh

cd "$(dirname "$0")"

/usr/sbin/eips -c
/usr/sbin/eips 15  4 'Starting GOES-19 satellite clock...'

# Delete old file
rm -f > ./goes_latest.png 
# Make sure there is enough time to reconnect to the wifi
# Refresh
python3 /mnt/base-us/extensions/goesclock/bin/clock.py
# fbink -c -g file=./goes_latest.png,w=800,halign=center,valign=center 
eips -g ./goes_latest.png
sleep 20
exit
