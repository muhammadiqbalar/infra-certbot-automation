from abc import ABC, abstractmethod
import subprocess
from models.command_result import CommandResult


class BaseRunner(ABC):
    @abstractmethod
    def run(self, command:list[str]) -> CommandResult:
        pass


class LocalRunner(BaseRunner):
    def run(self, command: list[str]) -> CommandResult:
       
        result = subprocess.run(
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
