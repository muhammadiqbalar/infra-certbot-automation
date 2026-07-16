from pathlib import Path
from cryptography import x509
from cryptography.hazmat.backends import default_backend

def check_certificate(cert_path: str):
    """
    Check whether the certificate file exists and parse its details.
    """
    cert_file = Path(cert_path)

    if not cert_file.exists():
        print(f"Error: Certificate file not found at {cert_path}")
        return False

    print("Certificate file found.")

    return True
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
