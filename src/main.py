import argparse
from pathlib import Path
from certbot.check import check_certificate


def main():

	parser = argparse.ArgumentParser(
	 description ="Infrastructure Certbot Automation"
	)

	subparser = parser.add_subparsers(dest="command")


	check_parser = subparser.add_parser("check")


	check_parser.add_argument(
		"--cert",
		type=Path,
		required=True,
		help="Certificate path"
	)


	args = parser.parse_args()

	if args.command == "check":
		check_certificate(args.cert)

if __name__ == "__main__":
   main()

