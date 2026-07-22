from certbot.runner import BaseRunner
from certbot.command_builder import build_certbot_command

from models.renewal_action import RenewalAction
from models.renewal_result import RenewalResult
from models.renewal_plan import RenewalPlan
from models.renewal_status import RenewalStatus

from utils.logger import setup_logger

logger=setup_logger()

def execute_renewal(runner: BaseRunner, plan: RenewalPlan, renew_config: dict,) -> RenewalResult:
    
    if plan.action != RenewalAction.RENEW:
       logger.info(
          f"[{plan.name}] Renewal Skipped"
       ) 

       return RenewalResult(

          name=plan.name,
          certbot_name=plan.certbot_name,
          status=RenewalStatus.SKIPPED,
          success=True,
          return_code=1,
          stdout="Skipped",
          stderr="",

       )
    
    logger.info(
      f"[{plan.name}] Executing renewal "
      f"({plan.certbot_name})"
    )

    command = build_certbot_command(
       renew_config=renew_config,
       certbot_name=plan.certbot_name,
    )
    result = runner.run(command)

    if result.success:
       logger.info(
         f"[{plan.name}] Renewal completed successfully"
       )
       return RenewalResult(

          name=plan.name,
          certbot_name=plan.certbot_name,
          status=RenewalStatus.SUCCESS,
          success=True,
          return_code=result.return_code,
          stdout=result.stdout,
          stderr=result.stderr,

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
       status=RenewalStatus.FAILED,
       success=False,
       return_code=result.return_code,
       stdout=result.stdout,
       stderr=result.stderr,
   )
