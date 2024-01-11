import serial
import time
import numpy as np

class UsbConnection:
	def __init__(self, port, name, is_verbose = False):
		self.port = port
		self.name = name
		self.is_verbose = is_verbose

		if is_verbose:
			print("\nConnecting to arduino...")

		self.arduino_usb = serial.Serial(port = port, baudrate = 9600)

		if is_verbose:
			print("    Connection successful!")

	def WriteData(self, x):
		x += "\0"
		byte_data = bytes(x,  'utf-8')

		self.arduino_usb.write(byte_data)
		time.sleep(0.05)

	def SendAngles(self, vector3):

		if self.is_verbose:
			print("\nSending angles", vector3, "...")

		position_string = str(int(vector3[0])) + "," + str(int(vector3[1])) + "," + str(int(vector3[2])) + ","

		self.WriteData(position_string)

		if self.is_verbose:
			print("    Angles sent successfully!")
