import argparse

def GetSystemArgs():
	print("")
	arg_parser = argparse.ArgumentParser()
	arg_parser.add_argument("-s", "--side", type = str, help = "which side of the controller the arm is sitting on, i.e. 'right' or 'left'")
	arg_parser.add_argument("-p", "--port", type = str, help = "the name of the USB port to use, i.e. 'COM5' or 'COM8'")

	args = arg_parser.parse_args()

	if args.port is None:
		print("    [Error]: You need to specify a USB port with the --port argument, i.e. --port 'COM5' or --port 'COM8'")
		exit()

	if args.side is None or not (args.side == "right" or args.side == "left"):
		print("    [Error]: You need to specify which side the arm is on with the --side argument, i.e. --side 'right' or --side 'left'")
		exit()

	return args
