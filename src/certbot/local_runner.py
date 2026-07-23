from subprocess import run

from certbot.runner import BaseRunner

from models.command_result import CommandResult


class LocalRunner(BaseRunner):
    def run(self, command: list[str]) -> CommandResult:

        result = run(
            command,
            capture_output=True,
            text=True,
        )


        return CommandResult(

            success=result.returncode ==0,
            return_code=result.returncode,
            stdout=result.stdout,
            stderr=result.stderr,
        )
