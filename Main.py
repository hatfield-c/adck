import time

import UsbConnection

def Main():
	action = None

	port = "COM8"
	name = "right_arm"
	usb_connection = None

	INIT = [85, 125, 72]

	FORWARD = [46, 110, 36]
	LEFT = [77, 139, 70]
	BACKWARD = [124, 139, 78]
	RIGHT = [90, 52, 0]

	while True:
		print("\n====================================")
		print("  Autononmous Drone Conversion Kit")
		print("          (ADCK v0.0.1)")
		print("       Calibration Interface\n")
		print("         by Cody Hatfield")
		print("====================================")

		print("\nWelcome to the ADCK Calibration Interface! Please select from the following options:")
		print("    0. Connect to Arduino")
		print("    1. FORWARD POSITION")
		print("    2. LEFT POSITION")
		print("    3. BACKWARD POSITION")
		print("    4. RIGHT POSITION")
		print("    5. CENTER POSITION")
		print("    6. Exit ADCK Calibration Interface")

		action = input("\n[Action]:")
		action = int(action)

		if action == 6:
			break

		if action == 0 and usb_connection is None:
			usb_connection = UsbConnection.UsbConnection(port = port, name = name, init = INIT, is_verbose = True)
		elif usb_connection is not None:
			if action == 1:
				usb_connection.SetPosition(FORWARD)
			if action == 2:
				usb_connection.SetPosition(LEFT)
			if action == 3:
				usb_connection.SetPosition(BACKWARD)
			if action == 4:
				usb_connection.SetPosition(RIGHT)
			if action == 5:
				usb_connection.SetPosition(INIT)
		else:
			print("\n[WARNING]: Must establish a connection to the arduino first.")

	if usb_connection is not None:
		usb_connection.arduino_usb.close()


if __name__ == "__main__":
	Main()
