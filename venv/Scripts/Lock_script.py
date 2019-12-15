#Important Links
# https://tutorials-raspberrypi.com/connecz-raspberry-pi-kecpad-code-lock/
import socket
import time
import pandas as pd
import RPi.GPIO as GPIO
import request
from keypad import keypad
# Create a socket object
# S socket object is to listen  a string which will be send by lock
# 5 minute is maximum expiration OTP
# This function will convert list into integer value
def convert(list):
    # Converting integer list to string list
    s = [str(i) for i in list]
    # Join list items using join()
    res = int("".join(s))
    return (res)

MAXIMUM_OTP_EXPIRATION_TIME = 5
socket_cloud = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
start_time = pd.datetime.now().minute
#print(pd.datetime.now().second)
print(start_time)
error_code = 000000
#OTP_DATABASE = [101010,708090,102030,101112]
Adifico_cloud_server_IP = '192.168.1.10'
Adifico_cloud_server_port = 9000
socket_cloud.connect((Adifico_cloud_server_IP, Adifico_cloud_server_port))
print("The socket has successfully connected to Adifico server having socket information",Adifico_cloud_server_IP,Adifico_cloud_server_port)
# Receive the OTP now through socket listening
# 1024 represent size of the string
OTP_data = socket_cloud.recv(1024)
KEY_PAD_DATA =KEY_PAD_INPUT()
# Now check the OTP data is equal to keypad data
if KEY_PAD_DATA == OTP_data:
    print("Given OTP matches with KEYPAD DATA",KEY_PAD_DATA)
    if OTP_data != error_code:
        print("Thanks GOD we are at safe zone ......!!!!!")
        end_time = pd.datetime.now().minute
        Difference_time =end_time - start_time
        if Difference_time <= MAXIMUM_OTP_EXPIRATION_TIME:
            print("Trigger the lock to open the door and see the magic inside the door")
        else:
            print("Do not trigger the lock OTP expire ,Please Note our expiry time is %d",MAXIMUM_OTP_EXPIRATION_TIME)
    else:
        print("We have error code OTP receive ,Danger Alert Someone is Tampering the data,Please add some encryptions")
else:
    print("Given OTP does not match with input keypad data")
#This function will take input from keypad and return integer keypad data with 6 digit
def KEY_PAD_INPUT():
    print("Please enter keypad input data")
    kp = keypad(columnCount=3)
    # waiting for a keypress
    digit = None
    while digit == None:
        digit = kp.getKey()
    # Print result
    print(digit)
    time.sleep(0.5)
    ###### 6 Digit wait ######
    seq = []
    for i in range(6):
        digit = None
        while digit == None:
            digit = kp.getKey()
            #This will append the digit in the list
        seq.append(digit)
        #Time interval between consecutive key press
        time.sleep(0.4)
    # Check digit code
    print("Sequence enter from the keypad are ",seq)
    # The sequence will be stored in form of list ,now it's time to convert into integer
    convert(seq)
    return seq
