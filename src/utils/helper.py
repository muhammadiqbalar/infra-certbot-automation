from colorama import Fore, Style
from models.status import CertificateStatus
from  datetime import datetime
from config.constants import DATE_FORMAT

status_colors = {
    "VALID": Fore.GREEN,
    "WARNING": Fore.YELLOW,
    "CRITICAL": Fore.MAGENTA,
    "EXPIRED": Fore.RED,    
}



def colorize_status(status: str) -> str:

    color = status_colors.get(status, Fore.WHITE)
    return f"{color}{status}{Style.RESET_ALL}"



def format_datetime(dt: datetime) -> str:
    """
    format datetime for display.
    returns:
      formatted datetime string or '-'
      if datetime is None.
    """
    if dt is None:
       return "-"

    return dt.strftime(DATE_FORMAT)
