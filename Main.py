import time

import UsbConnection

def Main():
	action = None

	port = "COM8"
	name = "right_arm"
	usb_connection = None

	FORWARD = [90, 110, 90]

	while True:
		print("\n==================================")
		print("  Autononmous Drone Conversion Kit")
		print("          (ADCK v0.0.1)")
		print("       Calibration Interface")
		print("         by Cody Hatfield")
		print("\n==================================")

		print("\nWelcome to the ADCK Calibration Interface! Please select from the following options:")
		print("    0. Connect to Arduino")
		print("    1. FORWARD POSITION")
		print("    2. LEFT POSITION")
		print("    3. BACKWARD POSITION")
		print("    4. RIGHT POSITION")
		print("    5. Exit ADCK Calibration Interface")

		action = input("\n[Action]:")
		action = int(action)

		if action == 5:
			break

		if action == 0 and usb_connection is None:
			usb_connection = UsbConnection.UsbConnection(port = port, name = name, is_verbose = True)
		elif usb_connection is not None:
			if action == 1:
				usb_connection.SetPosition(FORWARD)
		else:
			print("\n[WARNING]: Must establish a connection to the arduino first.")


if __name__ == "__main__":
	Main()
