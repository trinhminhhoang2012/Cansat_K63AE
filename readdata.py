import serial

class read:
    def __init__(self, COMport, transRate):
        self.COMport = COMport
        self.transRate = transRate

    #def __dataFilter(data)
    def read(self):
        ser = serial.Serial(self.COMport, self.transRate, timeout=2, xonxoff=False, rtscts=False, dsrdtr=False) #Tried with and without the last 3 parameters, and also at 1Mbps, same happens.
        ser.flushInput()
        ser.flushOutput()
        while True:
            line = ser.readline()
            
            line = str(line)
            print(line[0:6])
        