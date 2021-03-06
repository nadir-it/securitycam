#!/usr/bin/env bash
# for correct time logging add the following to jetson-inference/docker/run.sh
#Just after:
#	DATA_VOLUME="\
#	--volume $PWD/data:$DOCKER_ROOT/data \
#Add/Insert:
#	--volume /etc/timezone:/etc/timezone:ro \
#	--volume /etc/localtime:/etc/localtime:ro \
# The system will work without it but the time will be incorrect.
# Change the docker run options from -it to -i

#path to security camera control software to mount into container
volPath="--volume $HOME/securitycam:/securitycam"

#always use the run command argument LAST
runCameraCmd="--run /securitycam/detect.py --input-codec=h264 --output-codec=h265 --bitrate=2000000 $INURI $OUTURI"

(cd $HOME/jetson-inference && docker/run.sh $volPath $runCameraCmd)
#(cd $HOME/jetson-inference && docker/run.sh $volPath)

