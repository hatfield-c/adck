import serial
import time

arduino = serial.Serial(port = "COM6", baudrate = 9600, timeout = 0.1)

def write_data(x):
	byte_data = bytes(x,  'utf-8')
	#byte_data = bytes([int(x)])

	arduino.write(byte_data)
	#arduino.write(byte_data)

	time.sleep(0.05)

	return

while True:
	num = input("Enter a number: ")
	value  = write_data(num)
