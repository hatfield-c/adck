import time

import UsbConnection

def MainExample():
	action = None

	port = "COM8"
	name = "right_arm"
	usb_connection = None

	INIT = [85, 125, 72]

	FORWARD = [46, 110, 36]
	LEFT = [77, 139, 70]
	BACKWARD = [124, 139, 78]
	RIGHT = [90, 52, 0]

	usb_connection = UsbConnection.UsbConnection(port = port, name = name, is_verbose = True)

	time.sleep(10)
	usb_connection.SetPosition(FORWARD)
	time.sleep(1)
	usb_connection.SetPosition(RIGHT)
	time.sleep(0.3)
	usb_connection.SetPosition(LEFT)
	time.sleep(.4)
	usb_connection.SetPosition(INIT)
	time.sleep(1.5)
	usb_connection.SetPosition(BACKWARD)
	time.sleep(1)
	usb_connection.SetPosition(FORWARD)
	time.sleep(5)

	usb_connection.arduino_usb.close()

if __name__ == "__main__":
	MainExample()
