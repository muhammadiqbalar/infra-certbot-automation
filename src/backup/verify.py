from pathlib import Path


REQUIRED_FILES = [
  "cert.pem",
  "chain.pem",
  "fullchain.pem",
  "privkey.pem",
]


def verify_certificate_directory(source: Path) -> tuple[bool, list[str]]:

    missing = []

    for file_name in REQUIRED_FILES:
        if not (source / file_name).exists():
            missing.append(file_name)

    return len(missing) == 0, missing
