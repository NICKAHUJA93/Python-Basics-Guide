import json
import serial
from time import sleep
import requests
#url_server =
ser = serial.Serial ("/dev/ttyS0", 9600)    #Open port with baud rate

while True:
    received_data = ser.read()              #read serial port
    sleep(0.03)
    data_left = ser.inWaiting()             #check for remaining byte
    received_data += ser.read(data_left)
    print (received_data)                  #print received data
    # convert the receive data into json format
    temp = received_data[0:4];
    press = received_data[4:8];
    humidity = received_data[8:12];
    json1 = {"temp":temp,"pressure":press,"humidity":humidity};
    r = requests.post(url=url_server, data=json1)
    #ser.write(received_data)                #transmit data serially