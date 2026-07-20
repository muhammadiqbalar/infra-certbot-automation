from models.certificate import CertificateInfo
from utils.helper import colorize_status, format_datetime

def print_header(name: str) -> None:
    """
    Print certificate section header
    """
    
    print("=" * 60)
    print(f"Certificate : {name}")
    print(f"=" *60)

def print_certificate(info: CertificateInfo) -> None:
    """
    Print certificate  information
    """
    print(f"Common Name          : {info.common_name}")
    print(f"Subject              : {info.subject}")
    print(f"issuer               : {info.issuer}")
    print(f"Serial Number        : {info.serial_number}")
    print("DNS Names")
    if info.dns_names:
      for dns in info.dns_names:
          print(f"  - {dns}")
    else:
          print("   - None")


    print(f"Signature algorithm  : {info.signature_algorithm}")
    print(f"Public key algorithm : {info.public_key_algorithm}")
    print(f"Key Size             : {info.key_size} bits")
    
    print(f"Valid From           : "f"{format_datetime(info.valid_from)}")
    print(f"Valid Until          : "f"{format_datetime(info.valid_until)}")
    print(f"Remaining Days       : {info.remaining_days}")
    print(f"Status               : {colorize_status(info.status)}")
    
    print()

def print_error(error: Exception) -> None:
    """
    Print error message.
    """
    print(f"ERROR : {error}")
    print()
