import time
import argparse

import UsbConnection

def MainCalibration():
	print("")
	arg_parser = argparse.ArgumentParser()
	arg_parser.add_argument("-s", "--side", type = str, help = "which side of the controller the arm is sitting on, i.e. 'right' or 'left'")
	arg_parser.add_argument("-p", "--port", type = str, help = "the name of the USB port to use, i.e. 'COM5' or 'COM8'")

	args = arg_parser.parse_args()

	port = args.port
	side = args.side
	usb_connection = None

	if port is None:
		print("    [Error]: You need to specify a USB port with the --port argument, i.e. --port 'COM5' or --port 'COM8'")
		exit()

	if side is None or not (side == "right" or side == "left"):
		print("    [Error]: You need to specify which side the arm is on with the --side argument, i.e. --side 'right' or --side 'left'")
		exit()

	calibrations = {}

	if side == "right":
		calibrations["center"] = [85, 125, 72]
		calibrations["forward"]= [46, 110, 36]
		calibrations["left"]= [77, 139, 70]
		calibrations["backward"]= [124, 139, 78]
		calibrations["right"]= [90, 52, 0]

	if side == "left":
		calibrations["center"] = [81, 60, 145]
		calibrations["forward"]= [112, 16, 101]
		calibrations["left"]= [82, 99, 180]
		calibrations["backward"]= [53, 14, 95]
		calibrations["right"]= [80, 7, 90]

	action = None
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
			usb_connection = UsbConnection.UsbConnection(port = port, name = side, is_verbose = True)
		elif usb_connection is not None:
			if action == 1:
				usb_connection.SendAngles(calibrations["forward"])
			if action == 2:
				usb_connection.SendAngles(calibrations["left"])
			if action == 3:
				usb_connection.SendAngles(calibrations["backward"])
			if action == 4:
				usb_connection.SendAngles(calibrations["right"])
			if action == 5:
				usb_connection.SendAngles(calibrations["center"])
		else:
			print("\n[WARNING]: Must establish a connection to the arduino first.")

	if usb_connection is not None:
		usb_connection.arduino_usb.close()


if __name__ == "__main__":
	MainCalibration()
