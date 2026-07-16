import argparse

def main():
	parser = argparse.ArgumentParser(
	 description ="Infrastructure Certbot Automation"
	)

	parser.add_argument(
	 "command",
	 choices=["check"],
	 help="Command to execute"
	)

	args = parser.parse_args()


	if args.command == "check":
		print("Certificate Checker")

if __name__ == "__main__":
   main()

