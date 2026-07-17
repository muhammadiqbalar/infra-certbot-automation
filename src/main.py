import argparse
from pathlib import Path
from certbot.check import check_certificate
from utils.yaml_loader import load_yaml

BASE_DIR = Path(__file__).resolve().parent.parent

CONFIG_FILE = BASE_DIR / "config" / "config.yaml"


def run_check() -> None:
    """
    Load Certificate from configuration and check each certificate.
    """
    config = load_yaml(CONFIG_FILE)
    

    for cert in config["certificates"]:
        print("=" * 60)
        print(f"Certificate: {cert['name']}")
        print("=" * 60)

        try:
            cert_path = BASE_DIR / cert["path"]

            info = check_certificate(cert_path)

            print(f"Common Name     : {info.common_name}")
            print(f"Issuer          : {info.issuer}")
            print(f"Serial Number   : {info.serial_number}")
       	    print(f"Valid From      : {info.valid_from}")
            print(f"Valid Until     : {info.valid_until}")
            print(f"Remaining Days  : {info.remaining_days}")
            print(f"Status          : {info.status}")
        except Exception as err:
            print(f"ERROR : {err}")
        print()

def main() -> None:
    """
     Application entry point CLI.
    """

    parser = argparse.ArgumentParser(
      description ="Infrastructure Certbot Automation"
    )

    subparser = parser.add_subparsers(dest="command", required=True)

    subparser.add_parser(
         "check",
         help="Check certificate information"
    )

    args = parser.parse_args()

    if args.command == "check":
       run_check()

if __name__ == "__main__":
   main()

