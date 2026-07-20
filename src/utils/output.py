from models.certificate import CertificateInfo
from utils.helper import (
  colorize_status, 
  format_datetime,
)

from config.constants import SEPARTOR
from models.summary import Summary
from report.summary import STATUS_MAPPING
from models.status import CertificateStatus

LABEL_WIDTH = 20

def print_separator()-> None:
    """
    Print separator line.
    """
    print(SEPARTOR)


def print_header(name: str) -> None:
    """
    Print certificate section header
    """
    
    print_separator()
    print(f"Certificate : {name}")
    print_separator()

def print_row(label: str, value) -> None:
    """
    Print formatted key/value row.
    """
    print(f"{label:<{LABEL_WIDTH}} : {value}")

def print_status_row(status: CertificateStatus, value: int) -> None:
    label = status.value
    padding = "" * (LABEL_WIDTH - len(label))
    print(f"{colorize_status(label)}{padding} : {value}")

def print_list(label: str, values: list[str])-> None:
    """
    Print certificate information.
    """
    print(label)
    for item in values:
        print(f" -{item}")
   

def print_certificate(info: CertificateInfo) -> None:
    """
    Print certificate  information
    """
    print_row("Common Name", info.common_name)
    print_row("Subject", info.subject)
    print_row("issuer", info.issuer)
    print_row("Serial Number", info.serial_number)
    print_list("DNS Names", info.dns_names)
  
    print_row("Signature algorithm", info.signature_algorithm)
    print_row("Public key algorithm", info.public_key_algorithm)
    print_row("Key Size", f"{info.key_size} bits")
    
    print_row("Valid From",format_datetime(info.valid_from))
    print_row("Valid Until",format_datetime(info.valid_until))
    print_row("Remaining Days",info.remaining_days)
    print_row("Status",colorize_status(info.status.value))
    
def print_summary(summary: Summary) -> None:
    """
    Print certificate  information
    """
        
    print()
    print("Certificate Summary")
    print_separator()
    print_row("Total", summary.total)
    print()
    for status, field in STATUS_MAPPING.items():
       
       print_row(
         status.value,
         getattr(summary, field),
       )
    print_row("ERROR", summary.error)
    print_separator()


def print_error(message: str) -> None:
    """
    Print error message.
    """
    print(f"ERROR : {message}")


def print_success(message: str) -> None:
    """
    Print success message.
    """
    print(f"SUCCESS : {message}")
