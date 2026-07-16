from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from cryptography import x509
from cryptography.hazmat.backends import default_backend



@dataclass
class CertificateInfo:
    """
    Store parsed certificate information
    """
    subject: str
    issuer:str
    serial_number:str
    valid_from:datetime
    valid_until:datetime

def check_certificate():
    certificate = load_certificate(cert_path)
    info = get_certificate_info(certificate)

    print(info.subject)
    print(info.issuer)
    print(info.valid_until)

def load_certificate(cert_path: Path) -> x509.Certificate:

    """
    Load and parse a new PEM certificate.

    Args:
	cert_path: Path to the PEM certificate.
    Returns:
        x509.Certificate: Parsed certificate object.
    Raises:
        FileNotFoundError: If the certificate file does not exist.
	ValueError: If the file is not a valid PEM certificate.
    """
    if not cert_path.exists():
       raise FileNotFoundError(
       	f"Certificate file not found: {cert_path}"
       )
    with cert_path.open("rb") as file:
         cert_data = file.read()
    try:
         certificate = x509.load_pem_x509_certificate(
         	cert_data,
		default_backend()
         )
    except Exception as err:
        raise ValueError(
        	f"Failed to parse certificate: {cert_path}"
        ) from err
    return certificate


def get_certificate_info(certificate: x509.Certificate) -> CertificateInfo:

    """
    Extract important information from  X.509 certificate.
    """
   
    return CertificateInfo(

	subject=certificate.subject.rfc4514_string(),
	issuer=certificate.issuer.rfc4514_string(),
	serial_number=str(certificate.serial_number),
	valid_from=certificate.not_valid_before,
	valid_until=certificate.not_valid_after,
 	
    )


















    )

