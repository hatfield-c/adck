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
	calibrations["ready"] = np.array([91, 81, 30])
	calibrations["center"] = np.array([92, 89, 19])
	calibrations["forward"] = np.array([65, 112, 22])
	calibrations["left"] = np.array([86, 139, 74])
	calibrations["backward"] = np.array([132, 125, 67])
	calibrations["right"] = np.array([87, 53, 0])
	calibrations["top_right"] = np.array([87, 53, 0])
	calibrations["top_left"] = np.array([73, 147, 76])
	calibrations["bottom_right"] = np.array([124, 54, 0])
	calibrations["bottom_left"] = np.array([112, 147, 76])

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
	time.sleep(6)

	angle = converter.AlphaToBeta(np.array([0, 0.9]))
	usb_connection.SendAngles(angle)
	time.sleep(3)

	angle = converter.AlphaToBeta(np.array([0, 0]))
	usb_connection.SendAngles(angle)
	time.sleep(3)

	angle = converter.AlphaToBeta(np.array([1, 0]))
	usb_connection.SendAngles(angle)
	time.sleep(3)

	angle = converter.AlphaToBeta(np.array([0, 0]))
	usb_connection.SendAngles(angle)
	time.sleep(2)

	angle = converter.AlphaToBeta(np.array([0, 0.9]))
	usb_connection.SendAngles(angle)
	time.sleep(2)

	angle = converter.AlphaToBeta(np.array([0, 0]))
	usb_connection.SendAngles(angle)
	time.sleep(12)

	usb_connection.SendAngles(calibrations["ready"])
	time.sleep(3)

	usb_connection.arduino_usb.close()

if __name__ == "__main__":
	TestRightExample()
