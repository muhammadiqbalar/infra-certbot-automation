from dataclasses import dataclass, field
from datetime import datetime

from models.status import CertificateStatus

@dataclass
class CertificateInfo:
 """
 Parsed X.509 certificate information.
 """
 subject: str
 common_name: str
 issuer: str
 serial_number: str
 valid_from: datetime
 valid_until: datetime
 remaining_days: int
 status: CertificateStatus
 dns_names: list[str] = field(default_factory=list)
 signature_algorithm: str = ""
 public_key_algorithm: str = ""
 key_size: int = 0
 
