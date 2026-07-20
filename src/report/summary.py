from models.summary import Summary
from models.status import CertificateStatus
from models.certificate import CertificateInfo
from utils.helper import colorize_status


STATUS_MAPPING = {
 CertificateStatus.VALID: "valid",
 CertificateStatus.WARNING: "warning",
 CertificateStatus.CRITICAL: "critical",
 CertificateStatus.EXPIRED: "expired",
}



def update_summary(summary: Summary, info: CertificateInfo, ) -> None:
    """
    Update summary counters.
    """

    summary.total +=1

    field = STATUS_MAPPING.get(info.status)
    
    if field:
       setattr(
         summary,
         field,
         getattr(summary, field) + 1
       )
    

def update_error(summary: Summary, ) -> None:
    """
    Count processing errors.
    """

    summary.error += 1


"""def print_summary(summary: Summary, ) -> None:

    print()
    
    print("=" * 60 )
    
    print("Certificate Summary")

    print("=" * 60 )

    print( f"Total{'':<11}: {summary.total}")
    print()
    for status, field in STATUS_MAPPING.items():
        print(
           f"{colorize_status(status):<25}: {getattr(summary, field)}"
        )
    print(f"ERROR{'':<11}: {summary.error}")
    print("=" * 60)
"""
