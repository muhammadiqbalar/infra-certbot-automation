from enum import Enum

class CertificateStatus(Enum):
 """
 Certificate status based on remaining validity.
 """
 VALID = "VALID"
 WARNING = "WARNING"
 CRITICAL = "CRITICAL"
 EXPIRED = "EXPIRED"
 ERROR = "ERROR"
