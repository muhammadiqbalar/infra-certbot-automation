from dataclasses import dataclass
from models.renewal_status import RenewalStatus

@dataclass(slots=True)
class RenewalResult:
      name: str
      certbot_name: str
      status: RenewalStatus
      success: bool
      return_code: int
      stdout: str
      stderr: str
