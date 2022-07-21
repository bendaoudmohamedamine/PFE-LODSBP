from random import randrange
import time
from paho.mqtt import client as mqtt
import serial
import string
import pynmea2
broker ="mqtt.eclipseprojects.io"
client = mqtt.Client("C1")
client.connect(broker)

port="/dev/ttyAMA0"
ser=serial.Serial(port,baudrate=9600,timeout=0.5)
dataout =pynmea2.NMEAStreamReader()

while True:
    
    newdata=ser.readline()
    print(newdata)
    
    
        
        

    if newdata[0:6] == "$GNRMC":
         newmsg=pynmea2.parse(newdata)
         
         lat=newmsg.latitude
         lng=newmsg.longitude
         gps="Latitude=" +str(lat) + "and Longitude=" +str(lng)
         print(gps)
         client.publish("T1",lat)
         client.publish("T1",lng)
         print("publish"+gps+"to T1")
         time.sleep(10)
