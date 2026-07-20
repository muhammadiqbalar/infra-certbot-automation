from colorama import Fore, Style
from models.status import CertificateStatus


def colorize_status(status: CertificateStatus) -> str:

    colors ={
    	CertificateStatus.VALID: Fore.GREEN,
        CertificateStatus.WARNING: Fore.YELLOW,
        CertificateStatus.CRITICAL: Fore.MAGENTA,
        CertificateStatus.EXPIRED: Fore.RED,    
    }

    color = colors.get(status, Fore.WHITE)
    return f"{color}{status.value}{Style.RESET_ALL}"
