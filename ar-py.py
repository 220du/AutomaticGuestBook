import serial

ser = serial.Serial(
    port='COM7',
    baudrate=57600,
)

while True:
    if ser.readable():
        res = ser.readline()
        print(res.decode()[:len(res)-2])
