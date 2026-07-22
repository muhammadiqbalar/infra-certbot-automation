from typing import Any

def build_certbot_command(renew_config: dict[str, Any], certbot_name: str, ) -> list[str]:

    
    command =[
      renew_config.get("command", "certbot"),
      "renew",
      "--cert-name",
      certbot_name,
    ]
    
    if renew_config.get(
      "dry_run", 
      False,
    ):
       command.append("--dry-run")
 
    if renew_config.get(
      "force_renewal", 
      False,
    ):
       command.append("--force_renewal")
    if renew_config.get(
      "quiet",
      False,
    ):
       command.append("--quiet")
    return command

