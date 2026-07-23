from abc import ABC, abstractmethod
import subprocess
from models.command_result import CommandResult


class BaseRunner(ABC):
    @abstractmethod
    def run(self, command:list[str]) -> CommandResult:
        raise NotImplementedError


