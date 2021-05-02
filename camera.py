#!/usr/bin/env python3

import socket
import time
import picamera

cam_server = '192.168.10.50'

#spawn camera for performance reasons
camera = picamera.PiCamera()
camera.resolution = (1920, 1080)
camera.framerate = 24
camera.rotation = 270

#connect to server at port 8000
client_socket = socket.socket()
client_socket.connect((cam_server, 8000))

#make file object out of connection to write to
connection = client_socket.makefile('wb')

try:
    camera.start_recording(connection, format='h264')
    camera.wait_recording(60)
    camera.stop_recording()
finally:
    connection.close()
    client_socket.close()
