#Modified by smartbuilds.io
#Date: 01.05.22

import cv2
import numpy as np
import os
ds_factor=1

process_this_frame = True

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0) #Use this for USB cameras / non pi camera module
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()
        image=cv2.resize(image,None,fx=ds_factor,fy=ds_factor,interpolation=cv2.INTER_AREA)
        process_this_frame = True
        
        process_this_frame = not process_this_frame  
        
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

