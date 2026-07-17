from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.x509.oid import NameOID

@dataclass
class CertificateInfo:
    """
    Store parsed certificate information.
    """
    subject: str
    common_name: str
    issuer: str
    serial_number: str
    valid_from: datetime
    valid_until: datetime
    remaining_days: int
    status: str


def load_certificate(cert_path: Path) -> x509.Certificate:
    """
    Load and parse a PEM certificate.

    Args:
        cert_path: Path to the PEM certificate.

    Returns:
        Parsed X.509 certificate.

    Raises:
        FileNotFoundError: If the certificate file does not exist.
        ValueError: If the certificate cannot be parsed.
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
            default_backend(),
        )
    except Exception as err:
        raise ValueError(
            f"Failed to parse certificate: {cert_path}"
        ) from err

    return certificate


def calculate_remaining_days(valid_until: datetime) -> int:
    """
    Calculate remaining days until certificate expiration.
    """
    today = datetime.now(timezone.utc)
    return (valid_until - today).days


def determine_status(remaining_days: int) -> str:
    """
    Determine certificate status.
    """
    if remaining_days < 0:
        return "EXPIRED"
    elif remaining_days <= 46:
        return "WARNING"
    else:
        return "VALID"


def get_certificate_info(certificate: x509.Certificate) -> CertificateInfo:
    """
    Extract important information from an X.509 certificate.
    """

    valid_from = getattr(
        certificate,
        "not_valid_before_utc",
        certificate.not_valid_before_utc,
    )

    valid_until = getattr(
        certificate,
        "not_valid_after_utc",
        certificate.not_valid_after_utc,
    )

    remaining_days = calculate_remaining_days(valid_until)
    status = determine_status(remaining_days)

    return CertificateInfo(
        subject=certificate.subject.rfc4514_string(),
        common_name=certificate.subject.get_attributes_for_oid(NameOID.COMMON_NAME)[0].value,
        issuer=certificate.issuer.rfc4514_string(),
        serial_number=str(certificate.serial_number),
        valid_from=valid_from,
        valid_until=valid_until,
        remaining_days=remaining_days,
        status=status,
    )


def check_certificate(cert_path: str | Path) -> CertificateInfo:
    """
    Load a certificate and return its information.
    """
    cert_path = Path(cert_path)
    certificate = load_certificate(cert_path)
    return get_certificate_info(certificate)















