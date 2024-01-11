import time
import math
import numpy as np

import ConversionManifold
import UsbConnection

def MainExample():

	CENTER = np.array([85, 125, 72])
	RIGHT = np.array([90, 52, 0])
	FORWARD = np.array([46, 110, 36])
	LEFT = np.array([77, 139, 70])
	BACKWARD = np.array([124, 139, 78])
	TR_CORNER = np.array([39, 67, 0])
	TL_CORNER = np.array([66, 150, 89])
	BR_CORNER = np.array([120, 85, 0])
	BL_CORNER = np.array([101, 153, 90])

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
			CENTER,
			RIGHT,
			FORWARD,
			LEFT,
			BACKWARD,
			TR_CORNER,
			TL_CORNER,
			BR_CORNER,
			BL_CORNER
		]
	)

	port = "COM8"
	name = "right_arm"
	usb_connection = None

	usb_connection = UsbConnection.UsbConnection(port = port, name = name, is_verbose = True)

	time.sleep(7)
	usb_connection.SendAngles(CENTER)

	steps = 100
	spiral_angle = 0
	angle_step = (2 * math.pi) / steps
	for i in range(steps):
		radius = 1

		x_spiral = math.cos(spiral_angle)
		y_spiral = math.sin(spiral_angle)

		x_control = x_spiral * radius
		y_control = y_spiral * radius

		angle = converter.AlphaToBeta(np.array([x_control, y_control]))
		usb_connection.SendAngles(angle)

		spiral_angle += angle_step
		time.sleep(0.02)

	time.sleep(3)
	usb_connection.arduino_usb.close()

if __name__ == "__main__":
	MainExample()
