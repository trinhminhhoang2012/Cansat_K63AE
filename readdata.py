from dataclasses import dataclass
import serial
import re
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import style
import numpy as np
import time

def dataFilter(data):
    output = re.findall(r'\d+(?:\.\d+)?', data)
    if (output != None):
        if (len(output)>=8):
            return np.asarray(output)

def animate(i, xdata, ydata):
    line = ser.readline()
    line = str(line)
    print(line)
    session = dataFilter(line)
    if (isinstance(session, (np.ndarray))):
        xappend = float(session[0])/1000
        yappend = session[1]
        xdata.append(xappend)
        ydata.append(yappend)
        ydata.sort()
        xdata = xdata[-20:]
        ydata = ydata[-20:]
        ax.clear()
        ax.plot(xdata, ydata, label="Temperature")
        plt.xticks(rotation=45, ha='right')
        ax.set_ylim([0,50])
        #plt.legend()
        


COM_PortNumber = input(">Insert COM Port Number\n")
#transRate = int(input(">Insert Transfer Rate\n"))
#pattern = "//dev//ttyUSB0"
pattern = "COM"
COMport = pattern + str(COM_PortNumber)
transRate = 19200

ser = serial.Serial(COMport, transRate, timeout=2, xonxoff=False, rtscts=False, dsrdtr=False) #Tried with and without the last 3 parameters, and also at 1Mbps, same happens.
ser.flushInput()
ser.flushOutput()

xdata = []
ydata = []
fig, ax = plt.subplots()
ax.set_xlabel("Time (s)")
ax.set_ylabel("oC")
ani = FuncAnimation(fig, animate,fargs=(xdata,ydata), interval=500, repeat=False)        
plt.show()

                