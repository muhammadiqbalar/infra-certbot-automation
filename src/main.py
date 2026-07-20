import argparse
from pathlib import Path
from certbot.check import check_certificate
from utils.yaml_loader import load_yaml
from utils.logger import setup_logger
from utils.output import (
    print_certificate,
    print_error,
    print_header,
)

from models.summary import Summary
from report.summary import (
    update_summary,
    update_error,
    print_summary,
)


BASE_DIR = Path(__file__).resolve().parent.parent

CONFIG_FILE = BASE_DIR / "config" / "config.yaml"


logger = setup_logger()

def run_check() -> None:
    """
    Check all certificate define in config YAML.
    """
    logger.info("Starting certificate check")

    config = load_yaml(CONFIG_FILE)
    
    summary = Summary ()

    for cert in config["certificates"]:
        print_header(cert["name"])

        try:
            cert_path = BASE_DIR / cert["path"]

            logger.info(f"[{cert['name']}] Checking certificate")

            info = check_certificate(cert_path)

            update_summary(summary, info)

            print_certificate(info)

            logger.info(f"[{cert['name']}] Remaining Days: {info.remaining_days}")
            
            logger.info(f"[{cert['name']}] Status: {info.status.value}")

        except Exception as err:
            update_error(summary)
            logger.error(err)
            print_error(err)
        print()

    print_summary(summary)

    logger.info("Certificate check completed")

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

