#!/bin/bash
# -rot to rotate video feed
# -w and -h to set resolution
# -fps to set frame rate
# -b to set bandwidth limits

raspivid -o - -t 0 -rot 270 -w 1920 -h 1080 -fps 24 -b 2000000 | cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/stream}' :demux=h264  --verbose=2 --file-logging --logfile=vlc-log.txt
