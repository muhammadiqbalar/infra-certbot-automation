from configparser import ConfigParser
from pathlib import Path

DEFAULT_RENEWAL_DIR = Path("/etc/letsencrypt/renewal")

def read_authenticator(certbot_name: str, renewal_dir: Path = DEFAULT_RENEWAL_DIR,) -> str:

    config_file = renewal_dir / f"{certbot_name}.conf"
    if not config_file.exists():
       return "unknown"
    parser = ConfigParser()
 
    parser.read(config_file)
 
    return parser.get(
       "renewalparams",
       "authenticator",
       fallback="unknown",
    )
