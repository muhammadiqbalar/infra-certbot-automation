from pathlib import Path
from certbot.executor import execute_renewal
from certbot.renewal_header import read_authenticator
from certbot.renewal_planner import build_renewal_plan
from certbot.check import check_certificate
from certbot.local_runner import LocalRunner

from models.renewal_plan import RenewalPlan
from models.renewal_action import RenewalAction
from models.renewal_status import RenewalStatus
from utils.logger import setup_logger
from utils.yaml_loader import load_yaml


BASE_DIR = Path(__file__).resolve().parent.parent.parent

CONFIG_FILE = BASE_DIR / "config" / "config.yaml"

logger = setup_logger()

def run_renew() -> None:
    """
    Execute renewal planning.
    """
    config = load_yaml(CONFIG_FILE)

    renew_config = config["renew"]

    logger.info("Starting renewal planning")

    plans = build_renewal_plan()

    logger.info(
      f"Renewal planning completed ({len(plans)} certificate(s))"
    )
    runner = LocalRunner()
    success = 0
    failed = 0
    skipped = 0
    
    logger.info(
      f"Starting renewal execution"
    )

    for plan in plans:
        result = execute_renewal(
          runner=runner,
          plan=plan,
          renew_config=renew_config,
        )

        if result.status == RenewalStatus.SUCCESS:

           success += 1

        elif result.status == RenewalStatus.SKIPPED:
           skipped += 1

        else:
           failed +=1

    print()
    print("=" * 60)
    print("Renewal Summary")
    print("=" * 60)

    print(f"Success   : {success}")
    print(f"Failed    : {failed}")
    print(f"Skipped   : {skipped}")
    print("=" * 60)
    print()
    if  failed ==0:
        logger.info(
           f"Renewal completed successfully "
           f"({success} success, "
           f"{failed} failed, "
           f"{skipped} skipped)"
        )
    else:
        logger.warning(
           f"Renewal completed with errors "
           f"({success} success, "
           f"{failed} failed, "
           f"{skipped} skipped)"
        )    


