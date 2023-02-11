import serial

port = serial.Serial("/dev/ttyS0", baudrate=115200, timeout=3.0)

while True:
    rcv = ""
    rcv = port.read()
    if rcv != "":
        print(rcv)


