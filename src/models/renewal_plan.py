from dataclasses import dataclass

from models.renewal_action import RenewalAction

@dataclass(slots=True)
class RenewalPlan:
  name: str
  certbot_name: str
  path: str
  remaining_days: int
  authenticator: str
  action: RenewalAction
  
