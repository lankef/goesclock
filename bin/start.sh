#!/bin/sh

cd "$(dirname "$0")"

while true
do
    rm -f ./goes_latest.png > /dev/null 2>&1
    python3 /mnt/base-us/extensions/goesclock/bin/clock.py > /dev/null 2>&1
    eips -g ./goes_latest.png > /dev/null 2>&1
    sleep 5

    # non-blocking check for any touch within 0.1 seconds
    if sudo timeout 0.1 evtest --grab "$TOUCH_DEV" 2>&1 | grep -q "Event"; then
        echo "Detected touch; breaking loop."
        break
    fi
done

