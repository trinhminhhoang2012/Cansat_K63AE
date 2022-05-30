import serial
from readdata import read

COM_PortNumber = input(">Insert COM Port Number\n")
transRate = int(input(">Insert Transfer Rate\n"))
COMport = "COM" + str(COM_PortNumber)

COMread = read(COMport=COMport, transRate=transRate)
        