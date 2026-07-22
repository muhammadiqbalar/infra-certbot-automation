from dataclasses import dataclass

@dataclass(slots=True)
class CommandResult:
  success: bool
  return_code: int
  stdout: str
  stderr: str
