#!/usr/bin/env python3

import os
import sys
from datetime import date
from datetime import datetime
from pathlib import Path


def getLogFilename():
	timestamp = datetime.now()		#get a time stamp for messaging and logging of security data
	month = timestamp.strftime("%m")	#month as a number
	day = timestamp.strftime("%d")		#day as number
	year = timestamp.strftime("%Y")	#year as a number
	filename = "/securitycam/{}-{}-{}.log".format(year, month, day)
	return filename

def createLogMsg(objectsDetected):
	timestamp = datetime.now()		#get a time stamp for messaging and logging of security data
	#logtime = timestamp.strftime("%X")	#time in local format
	loghour = timestamp.strftime("%H")	#hour of day event occured
	logminute = timestamp.strftime("%M")	#minute of day event occured
	logtime = "{}:{}".format(loghour, logminute)
	buffer = ""
	for things in objectsDetected.keys():
		if objectsDetected[things] > 0:
			buffer = "Saw {} {}(s) at {}.\n".format(objectsDetected[things], things, logtime) + buffer
	return buffer

def writeLogMsg(msg):
	logfile = open(getLogFilename(), "a")
	logfile.write(msg)
	logfile.close()

#if __name__ == "__main__":
	#test script


