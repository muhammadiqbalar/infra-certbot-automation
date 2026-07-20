from models.summary import Summary
from models.status import CertificateStatus
from models.certificate import CertificateInfo
from utils.helper import colorize_status


STATUS_FIELDS = [
 (CertificateStatus.VALID, "valid"),
 (CertificateStatus.WARNING, "warning"),
 (CertificateStatus.CRITICAL, "critical"),
 (CertificateStatus.EXPIRED, "expired"),
]



def update_summary(summary: Summary, info: CertificateInfo, ) -> None:
    """
    Update summary counters.
    """

    summary.total +=1

    if info.status == CertificateStatus.VALID:
       summary.valid += 1
    elif info.status == CertificateStatus.WARNING:
       summary.warning += 1
    elif info.status == CertificateStatus.CRITICAL:
       summary.critical += 1
    elif info.status == CertificateStatus.EXPIRED:
       summary.expired += 1


def update_error(summary: Summary, ) -> None:
    """
    Count processing errors.
    """

    summary.error += 1


def print_summary(summary: Summary, ) -> None:

    print()
    
    print("=" * 60 )
    
    print("Certificate Summary")

    print("=" * 60 )

    print( f"Total          : {summary.total}")
    print()

    for status, field in STATUS_FIELDS:
        print(
           f"{colorize_status(status):<25}:"
           f"{getattr(summary, field)}"
        )
   
    print(f"ERROR{'':<11}:{summary.error}")

    print("=" * 60)
