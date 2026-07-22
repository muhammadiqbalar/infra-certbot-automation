import argparse

from certbot.check import run_check
from certbot.renew import run_renew
from backup.backup import run_backup


def main() -> None:
    """
     Application entry point CLI.
    """

    parser = argparse.ArgumentParser(
      description ="Infrastructure Certbot Automation"
    )

    parser.add_argument(
      "command",
      choices=[
        "check",
        "backup",
        "renew",
        "deploy",
        "validate",
      ],
      help="Automation Command",
    )

    args = parser.parse_args()

    if args.command == "check":
       run_check()
    if args.command == "backup":
       run_backup()
    if args.command == "renew":
       run_renew()

if __name__ == "__main__":
   main()

