import argparse
from pathlib import Path
from certbot.check import check_certificate


def main():

	parser = argparse.ArgumentParser(
	 description ="Infrastructure Certbot Automation"
	)

	subparser = parser.add_subparsers(dest="command", required=True)


	check_parser = subparser.add_parser("check")


	check_parser.add_argument(
		"--cert",
		type=Path,
		required=True,
		help="Certificate path"
	)


	args = parser.parse_args()
	try:
		if args.command == "check":
			info=check_certificate(args.cert)
			print("=" * 60)
			print("Certificate Information")
			print("=" * 60)

			print(f"Common Name     : {info.common_name}")
			print(f"Issuer          : {info.issuer}")
			print(f"Serial Number   : {info.serial_number}")
			print(f"Valid From      : {info.valid_from}")
			print(f"Valid Until     : {info.valid_until}")
			print(f"Remaining Days  : {info.remaining_days}")
			print(f"Status          : {info.status}")
	except Exception as err:
		print(f"ERROR : {err}")
if __name__ == "__main__":
   main()

