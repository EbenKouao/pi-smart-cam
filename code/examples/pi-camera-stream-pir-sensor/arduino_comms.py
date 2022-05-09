#!/usr/bin/env python3
#Description: Arduino -> Pi Comms for reading PIR Sensor Values

import serial
import time
from email_notification import sendMessage
import sys
from camera import VideoCamera

def take_picture(pi_email, pi_app_password, pi_port, pi_host, frame):
    try:
        print("Sending Notification..")
        sendMessage(pi_email, pi_app_password, pi_port, pi_host, frame)
        print("Notification Sent.")
    except:
        print("Error Sending Notification: ", sys.exc_info()[0])

def arduino_pi_comms(ser, sensitivity_timer, current_time, pi_email, pi_app_password, pi_port, pi_host, frame):
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
                   
            print("Time since last motion detected: ",time.time()- current_time)
            
            if(line == "1"): #if pir sensor value = 1/high
                detected = True
            
            # only send email notification if motion is detected after X seconds
            if(int(time.time() - current_time) > sensitivity_timer):
                
                current_time = time.time()
                print(line) # print output from Arduino Comms
                if(detected == True):
                    detected = False
                    take_picture(pi_email, pi_app_password, pi_port, pi_host, frame)
                    print("email sent")

# local testing
# arduino_pi_comms(ser, sensitivity_timer, current_time, pi_email, pi_app_password, pi_port, pi_host)