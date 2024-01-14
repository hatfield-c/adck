import Cli
import UsbConnection

def MainCalibration():
	args = Cli.GetSystemArgs()

	port = args.port
	side = args.side
	usb_connection = None

	calibrations = {}

	if side == "right":
		calibrations["ready"] = [91, 81, 30]
		calibrations["center"] = [92, 89, 19]
		calibrations["forward"]= [65, 112, 22]
		calibrations["left"]= [86, 139, 74]
		calibrations["backward"]= [132, 125, 67]
		calibrations["right"]= [87, 53, 0]
		calibrations["top_right"] = [87, 53, 0]
		calibrations["top_left"] = [73, 147, 76]
		calibrations["bottom_right"] = [124, 54, 0]
		calibrations["bottom_left"] = [112, 147, 76]

	if side == "left":
		calibrations["ready"] = [78, 62, 132]
		calibrations["center"] = [78, 69, 160]
		calibrations["forward"]= [111, 26, 122]
		calibrations["left"]= [80, 105, 180]
		calibrations["backward"]= [44, 26, 122]
		calibrations["right"]= [81, 16, 105]
		calibrations["top_right"] = [93, 25, 112]
		calibrations["top_left"] = [123, 91, 180]
		calibrations["bottom_right"] = [57, 23, 112]
		calibrations["bottom_left"] = [43, 91, 180]

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
		print("    1. READY")
		print("    2. CENTER")
		print("    3. FORWARD")
		print("    4. LEFT")
		print("    5. BACKWARD")
		print("    6. RIGHT")
		print("    7. TOP RIGHT")
		print("    8. TOP LEFT")
		print("    9. BOTTOM RIGHT")
		print("    10. BOTTOM LEFT")
		print("    11. Exit ADCK Calibration Interface")

		action = input("\n[Action]:")
		action = int(action)

		if action == 11:
			break

		if action == 0 and usb_connection is None:
			usb_connection = UsbConnection.UsbConnection(port = port, name = side, is_verbose = True)
		elif usb_connection is not None:
			if action == 1:
				usb_connection.SendAngles(calibrations["ready"])
			if action == 2:
				usb_connection.SendAngles(calibrations["center"])
			if action == 3:
				usb_connection.SendAngles(calibrations["forward"])
			if action == 4:
				usb_connection.SendAngles(calibrations["left"])
			if action == 5:
				usb_connection.SendAngles(calibrations["backward"])
			if action == 6:
				usb_connection.SendAngles(calibrations["right"])
			if action == 7:
				usb_connection.SendAngles(calibrations["top_right"])
			if action == 8:
				usb_connection.SendAngles(calibrations["top_left"])
			if action == 9:
				usb_connection.SendAngles(calibrations["bottom_right"])
			if action == 10:
				usb_connection.SendAngles(calibrations["bottom_left"])
		else:
			print("\n[WARNING]: Must establish a connection to the arduino first.")

	if usb_connection is not None:
		usb_connection.arduino_usb.close()


if __name__ == "__main__":
	MainCalibration()
