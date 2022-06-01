import time
import requests
import math
import random
import serial
import re
import numpy as np




TOKEN = "BBFF-CefUflEcwak6drfTLLrgmOh0oILI7V"  # Put your TOKEN here
DEVICE_LABEL = "CANSAT-GROUP3"  # Put your device label here 
#VARIABLE_LABEL_1 = "Time"  # Put your first variable label here
VARIABLE_LABEL_1 = "Temperature"  # Put your second variable label here
VARIABLE_LABEL_2 = "Pressure"  # Put your second variable label here
VARIABLE_LABEL_3 = "Alttitude"
VARIABLE_LABEL_4 = "Humidity"
VARIABLE_LABEL_5 = "Roll"
VARIABLE_LABEL_6 = "Pitch"
VARIABLE_LABEL_7 = "Yaw"


def dataFilter(data):
    output = re.findall(r'\d+(?:\.\d+)?', data)
    if (output != None):
        if (len(output)>=8):
            return np.asarray(output)


def build_payload(data, variable_1, variable_2, variable_3, variable_4, variable_5, variable_6, variable_7):
    # Creates two random values for sending data
    value_1 = data[1] #temp
    value_2 = data[2] #pressure
    value_3 = data[3] #alttitude
    value_4 = data[4] #humidity
    value_5 = data[5] #roll
    value_6 = data[6] #pitch
    value_7 = data[7] #yaw

    payload = {variable_1: value_1,
               variable_2: value_2,
               variable_3: value_3,
               variable_4: value_4,
               variable_5: value_5,
               variable_6: value_6,
               variable_7: value_7
    }
    return payload


def post_request(payload):
    # Creates the headers for the HTTP requests
    url = "http://industrial.api.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}

    # Makes the HTTP requests
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.post(url=url, headers=headers, json=payload)
        status = req.status_code
        attempts += 1
        time.sleep(1)

    # Processes results
    print(req.status_code, req.json())
    if status >= 400:
        print("[ERROR] Could not send data after 5 attempts, please check \
            your token credentials and internet connection")
        return False

    print("[INFO] request made properly, your device is updated")
    return True


def main(data):
    payload = build_payload(data,
        VARIABLE_LABEL_1, VARIABLE_LABEL_2, VARIABLE_LABEL_3, 
        VARIABLE_LABEL_4, VARIABLE_LABEL_5, VARIABLE_LABEL_6, 
        VARIABLE_LABEL_7)

    print("[INFO] Attemping to send data")
    post_request(payload)
    print("[INFO] finished")


if __name__ == '__main__':
    COM_PortNumber = input(">Insert COM Port Number\n")
    #transRate = int(input(">Insert Transfer Rate\n"))
    #pattern = "//dev//ttyUSB0"
    pattern = "COM"
    COMport = pattern + str(COM_PortNumber)
    transRate = 19200
    ser = serial.Serial(COMport, transRate, timeout=2, xonxoff=False, rtscts=False, dsrdtr=False) #Tried with and without the last 3 parameters, and also at 1Mbps, same happens.
    ser.flushInput()
    ser.flushOutput()
    while (True):
        line = ser.readline()
        line = str(line)
        print(line)
        session = dataFilter(line)
        if (isinstance(session, (np.ndarray))):
            main(session)
            time.sleep(0.050)