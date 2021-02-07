#!/usr/bin/env python3

#import os
import sys
import argparse

import seccamlog
import jetson.inference
import jetson.utils

parser = argparse.ArgumentParser(description="Detect people in live camera streams using DNNs and output to logfiles for messaging.")

parser.add_argument("input_URI", type=str, default="", nargs='?', help="URI of the input stream")
parser.add_argument("output_URI", type=str, default="", nargs='?', help="URI of the output stream")
parser.add_argument("--network", type=str, default="ssd-mobilenet-v2", help="pre-trained model to load (see below for options)")
parser.add_argument("--overlay", type=str, default="box,labels,conf", help="detection overlay flags (e.g. --overlay=box,labels,conf)\nvalid combinations are:  'box', 'labels', 'conf', 'none'")
parser.add_argument("--threshold", type=float, default=0.5, help="minimum detection threshold to use") 
parser.add_argument("--input-codec", type=str, default="", help="input stream codec i.e. h264, h265 mjpeg, vp9, etc.")
parser.add_argument("--output-codec", type=str, default="", help="input stream codec i.e. h264, h265 mjpeg, vp9, etc.")

try:
	opt = parser.parse_known_args()[0]
except:
	print("")
	parser.print_help()
	sys.exit(0)

#load detection neural network
net = jetson.inference.detectNet(opt.network, sys.argv, opt.threshold)
camera1 = jetson.utils.videoSource(opt.input_URI, argv=sys.argv)  #or csi://0 for example

#display is a video output for testing/local purposes. Final system should stream to a server for storage.
display = jetson.utils.videoOutput(opt.output_URI, argv=sys.argv) # "display://0" or 'my_video.mp4' for file or for remote streaming rtp://<remote-ip>:1234


#before transfer learning we only care about a small number of items the NN can detect
#detectionList = ['person', 'car', 'truck', 'motorcycle', 'bicycle', 'bus', 'dog', 'cat', 'umbrella', 'skateboard']
detectionList = ['person', 'car', 'truck', 'motorcycle', 'bicycle', 'bus', 'dog', 'cat']

logmsg = ''
lastlogmsg = ''


while True:
	img = camera1.Capture(format='rgb8')
	detections = net.Detect(img)
	#objectCount = len(detections)
	count=0
	detectionCount = {'person': 0, 'car':0, 'truck':0, 'motorcycle':0, 'bicycle':0, 'bus':0, 'dog':0, 'cat':0 }
	for thing in detections:
		objectDetected = net.GetClassDesc(thing.ClassID)
		if objectDetected in detectionList:
			count = detectionCount[objectDetected] + 1
			detectionCount.update({objectDetected:count})
	logmsg = seccamlog.createLogMsg(detectionCount)
	if logmsg != lastlogmsg:
		seccamlog.writeLogMsg(logmsg)
				#print(logmsg)
	lastlogmsg = logmsg
	
	display.Render(img)
	#testoutput.Render(img)
	display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))

	if not display.IsStreaming() or not camera1.IsStreaming():
		break

print("Camera 1 Feed DOWN!!!!")
