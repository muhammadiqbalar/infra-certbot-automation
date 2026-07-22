from certbot.runner import BaseRunner

from models.renewal_action import RenewalAction
from models.renewal_result import RenewalResult
from models.renewal_plan import RenewalPlan


from utils.logger import setup_logger

logger=setup_logger()

def execute_renewal(runner: BaseRunner, plan: RenewalPlan,) -> RenewalResult:
    
    if plan.action != RenewalAction.RENEW:
       logger.info(
          f"[{plan.name}] Renewal Skipped"
       ) 

       return RenewalResult(

          name=plan.name,
          certbot_name=plan.certbot_name,
          success=True,
          return_code=0,
          stdout="Skipped",
          stderr="",

       )
    
    logger.info(
      f"[{plan.name}] Executing renewal "
      f"({plan.certbot_name})"
    )


    result = runner.run(
       [
         "sudo",
         "certbot",
         "renew",
       ]
    )
    if result.success:
       logger.info(
         f"[{plan.name}] Renewal completed successfully"
       )
    else:
      logger.error(
         f"[{plan.name}] Renewal failed "
         f"(Return Code ={result.return_code})"
      )
      if result.stderr.strip():
         logger.error(
           result.stderr.strip()
         )
        
    return RenewalResult(
       name=plan.name,
       certbot_name=plan.certbot_name,
       success=result.return_code == 0,
       return_code=result.return_code,
       stdout=result.stdout,
       stderr=result.stderr,
   )
