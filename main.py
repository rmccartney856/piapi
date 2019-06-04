#NAME:  main.py
#DATE:  Wednesday 5th June 2019
#AUTH:  Ryan McCartney, EEE Undergraduate, Queen's University Belfast
#DESC:  A python function for running a cherrpi API as a serial pass through
#COPY:  Copyright 2018, All Rights Reserved, Ryan McCartney

import threading
import cherrypy
import serial
import time
import os

#Connection Status
leftArmActive = False
rightArmActive = False

try:
    
    try:
        leftArm = serial.Serial('/dev/ttyACM0')
        leftArmActive = True
        print("INFO: Connected to Left Arm")
    except:
        leftArmActive = False
        print("INFO: Failed to connect to Left Arm")
        
    try:
        rightArm = serial.Serial('/dev/ttyACM1')
        rightArmActive = True
        print("INFO: Connected to Right Arm")
    except:
        rightArmActive = False
        print("INFO: Failed to connect to Right Arm")

    class API(object):
        @cherrypy.expose
        def index(self):
            with open ("index.html", "r") as webPage:
                contents=webPage.readlines()
            return contents

        def send(self,command="this"):
            print("INFO: Sending '"+data+"' to robotic arm serial line.")
            return data
            

    if __name__ == '__main__':
        cherrypy.config.update({
            '/favicon.ico': {
            'tools.staticfile.on': True,
            'tools.staticfile.filename': os.path.join(os.getcwd(), 'favicon.ico')
            }
        })
        cherrypy.tree.mount(API())
        cherrypy.engine.start()
        cherrypy.engine.block()
        
except:
    print("ERROR: Main sequence error.")
