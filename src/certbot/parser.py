from cryptography import x509
from cryptography.x509.oid import NameOID


def get_common_name(certificate: x509.Certificate) -> str:
    """
    Return Common Name (CN).
    """
    try:
        return certificate.subject.get_attributes_for_oid(
            NameOID.COMMON_NAME
        )[0].value
    except IndexError:
        return "N/A"


def get_subject(certificate: x509.Certificate) -> str:
    """
    Return full subject.
    """
    return certificate.subject.rfc4514_string()


def get_issuer(certificate: x509.Certificate) -> str:
    """
    Return certificate issuer.
    """
    return certificate.issuer.rfc4514_string()


def get_serial_number(certificate: x509.Certificate) -> str:
    """
    Return serial number.
    """
    return str(certificate.serial_number)


def get_dns_names(certificate: x509.Certificate) -> list[str]:
    """
    Return Subject Alternative Names (SAN).
    """
    try:
        san = certificate.extensions.get_extension_for_class(
            x509.SubjectAlternativeName
        )

        return san.value.get_values_for_type(
            x509.DNSName
        )

    except x509.ExtensionNotFound:
        return []


def get_signature_algorithm(
    certificate: x509.Certificate,
) -> str:
    """
    Return signature hash algorithm.
    """
    try:
        return certificate.signature_hash_algorithm.name
    except Exception:
        return "Unknown"


def get_public_key_algorithm(
    certificate: x509.Certificate,
) -> str:
    """
    Return public key algorithm.
    """

    public_key = certificate.public_key()

    return public_key.__class__.__name__


def get_key_size(
    certificate: x509.Certificate,
) -> int:
    """
    Return public key size.
    """

    public_key = certificate.public_key()

    if hasattr(public_key, "key_size"):
        return public_key.key_size

    return 0
