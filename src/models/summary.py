from dataclasses import dataclass


@dataclass
class summary:
 total: int = 0
 valid: int = 0
 warning: int = 0
 critical: int = 0
 expired: int = 0
 error: int = 0
