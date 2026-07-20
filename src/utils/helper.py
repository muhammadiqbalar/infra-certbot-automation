from colorama import Fore, Style
from models.status import CertificateStatus
from  datetime import datetime


def colorize_status(status: CertificateStatus) -> str:

    colors ={
    	CertificateStatus.VALID: Fore.GREEN,
        CertificateStatus.WARNING: Fore.YELLOW,
        CertificateStatus.CRITICAL: Fore.MAGENTA,
        CertificateStatus.EXPIRED: Fore.RED,    
    }

    color = colors.get(status, Fore.WHITE)
    return f"{color}{status.value}{Style.RESET_ALL}"

def format_datetime(dt: datetime) -> str:
    """
    format datetime for display.
    returns:
      formatted datetime string or '-'
      if datetime is None.
    """
    if dt is None:
       return "-"

    return dt.strftime("%Y-%m-%d %H:%M UTC")
