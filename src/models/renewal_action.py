from enum import Enum


class RenewalAction(str, Enum):
      
      SKIP = "SKIP"
      RENEW = "RENEW"
      MANNUAL = "MANUAL"
