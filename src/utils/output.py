from certbot.check import CertificateInfo

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
    print(f"Common Name     : {info.common_name}")
    print(f"Issuer          : {info.issuer}")
    print(f"Serial Number   : {info.serial_number}")
    print(f"Valid From      : {info.valid_from}")
    print(f"Valid Until     : {info.valid_until}")
    print(f"Remaining Days  : {info.remaining_days}")
    print(f"Status          : {info.status}")
    
    print()

def print_error(error: Exception) -> None:
    """
    Print error message.
    """
    print(f"ERROR : {error}")
    print()
