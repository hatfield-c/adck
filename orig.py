import serial
import time
import numpy as np

arduino = serial.Serial(port = "COM8", baudrate = 9600, timeout = 0.1)

print("\nConnection established!")
print("    Press enter to begin...")
input()

def write_data(x):
	x += "\0"
	byte_data = bytes(x,  'utf-8')
	#byte_data = bytes([int(x)])

	arduino.write(byte_data)
	#arduino.write(byte_data)

	time.sleep(0.05)

	return

thetas = np.array([90, 90, 90])

print("\nSetup complete!")
print("    Sending control signals...\n")

for i in range(1):
	print("thetas:", thetas)

	theta_str = str(int(thetas[0])) + "," + str(int(thetas[1])) + "," + str(int(thetas[2])) + ","

	write_data(theta_str)
	thetas += 1

	time.sleep(0.5)

print("\nProgram complete!")
print("    Exiting...")