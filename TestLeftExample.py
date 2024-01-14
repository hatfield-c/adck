import time
import math
import numpy as np

import ConversionManifold
import UsbConnection
import Cli

def TestRightExample():
	args = Cli.GetSystemArgs()

	port = args.port
	side = args.side
	usb_connection = None

	calibrations = {}
	calibrations["ready"] = np.array([78, 62, 132])
	calibrations["center"] = np.array([78, 69, 160])
	calibrations["forward"] = np.array([111, 26, 122])
	calibrations["left"] = np.array([80, 105, 180])
	calibrations["backward"] = np.array([44, 26, 122])
	calibrations["right"] = np.array([81, 16, 105])
	calibrations["top_right"] = np.array([93, 25, 112])
	calibrations["top_left"] = np.array([123, 91, 180])
	calibrations["bottom_right"] = np.array([57, 23, 112])
	calibrations["bottom_left"] = np.array([43, 91, 180])

	converter = ConversionManifold.ConversionManifold(
		alpha_keys = [
			np.array([0, 0]),
			np.array([1, 0]),
			np.array([0, 1]),
			np.array([-1, 0]),
			np.array([0, -1]),
			np.array([1, 1]),
			np.array([-1, 1]),
			np.array([1, -1]),
			np.array([-1, -1]),
		],
		beta_keys = [
			calibrations["center"],
			calibrations["right"],
			calibrations["forward"],
			calibrations["left"],
			calibrations["backward"],
			calibrations["top_right"],
			calibrations["top_left"],
			calibrations["bottom_right"],
			calibrations["bottom_left"]
		]
	)

	usb_connection = UsbConnection.UsbConnection(port = port, name = side, is_verbose = True)
	time.sleep(10)

	usb_connection.SendAngles(calibrations["ready"])
	input("Press enter to continue...")

	usb_connection.SendAngles(calibrations["center"])
	time.sleep(3)

	angle = converter.AlphaToBeta(np.array([0, 1]))
	usb_connection.SendAngles(angle)
	time.sleep(3)

	angle = converter.AlphaToBeta(np.array([0, 0]))
	usb_connection.SendAngles(angle)
	time.sleep(13)

	angle = converter.AlphaToBeta(np.array([0, -1]))
	usb_connection.SendAngles(angle)
	time.sleep(12)

	usb_connection.SendAngles(calibrations["ready"])
	time.sleep(3)

	usb_connection.arduino_usb.close()

if __name__ == "__main__":
	TestRightExample()
