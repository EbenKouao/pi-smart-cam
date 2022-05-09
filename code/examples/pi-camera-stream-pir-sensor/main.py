#!/usr/bin/env python3
"""
Modified by smartbuilds.io
Date: 07.05.22

# main.py
Desc: This web application serves a motion JPEG stream and sends an image
notification to your email on motion detected via pir sensor

# install the necessary packages
"""
from flask import Flask, render_template, Response, request
from camera import VideoCamera
from arduino_comms import arduino_pi_comms
import time
import threading
import os
import sys
import serial

current_time = time.time() #initialise current time on run

# How long before ACK motion and sending notification
sensitivity_timer = 30

# View email_notification for setup
pi_email = "<app-email>"
pi_app_password = "<app-password>"
pi_port = 465
pi_host = "smtp.gmail.com"

pi_camera = VideoCamera(flip=False) # flip pi camera if upside down.

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') #you can customze index.html here

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def gen_capture(camera):
    frame = camera.get_frame()
    return frame
        
@app.route('/video_feed')
def video_feed():
    return Response(gen(pi_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    # device USB name e.g. /dev/ttyACM0 or /dev/ttyUSB0 if connected
    try:
        ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
        ser.reset_input_buffer()
        
        if ser:
            # Create thread for parallel processing/ multithreading
            arduino_comms_thread = threading.Thread(target=arduino_pi_comms, args=(ser, sensitivity_timer, current_time, pi_email, pi_app_password, pi_port, pi_host, gen_capture(pi_camera)))
            arduino_comms_thread.daemon = True
            arduino_comms_thread.start()
    except:
        print("Arduino not recognised")
        
    app.run(host='0.0.0.0', debug=False)
    