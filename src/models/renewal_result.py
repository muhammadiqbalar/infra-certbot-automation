from dataclasses import dataclass

@dataclass(slots=True)
class RenewalResult:
      name: str
      certbot_name: str
      success: bool
      return_code: int
      stdout: str
      stderr: str
