from pathlib import Path


from certbot.check import check_certificate
from certbot.renewal_header import read_authenticator


from models.renewal_action import RenewalAction
from models.renewal_plan import RenewalPlan

from utils.logger import setup_logger
from utils.yaml_loader import load_yaml

logger = setup_logger()

BASE_DIR = Path(__file__).resolve().parent.parent.parent

CONFIG_FILE = BASE_DIR / "config" / "config.yaml"


def build_renewal_plan()->list[RenewalPlan]:
    
    config = load_yaml(CONFIG_FILE)

    warning_days = config["certificate"]["warning_days"]

    plans: list[RenewalPlan] = []

    for cert in config["certificates"]:

        logger.info(f"[{cert['name']}] Building renewal plan")

        # Ambil informasi certificate
        certificate = check_certificate(
            Path(cert["source_path"])
        )
        
        # Baca authenticator dari renewal.conf
        authenticator = (
           read_authenticator(
            cert["certbot_name"]
           )
           .strip()
           .lower()
        )
 
        # Tentukan action
        if authenticator == "manual":

            action = RenewalAction.MANUAL

        elif certificate.remaining_days <= warning_days:

            action = RenewalAction.RENEW

        else:

            action = RenewalAction.SKIP

        # Buat RenewalPlan
        plan = RenewalPlan(
            name=cert["name"],
            certbot_name=cert["certbot_name"],
            path=cert["path"],
            authenticator=authenticator,
            remaining_days=certificate.remaining_days,
            action=action,
        )

        plans.append(plan)

        logger.info(
            f"[{plan.name}] "
            f"{plan.remaining_days} days remaining | "
            f"Authenticator={plan.authenticator} | "
            f"Action={plan.action.value}"
        )
        
    return plans
