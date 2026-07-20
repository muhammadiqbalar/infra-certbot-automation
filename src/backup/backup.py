from pathlib import Path
import shutil
from datetime import datetime



def create_backup_directory(base_dir: Path) -> Path:
    """
    Create timestamped backup directory.
    Example:
    backups/
      20260720_150512/
    """


    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    backup_dir = base_dir / timestamp

    backup_dir.mkdir(
 
      parents=True,
      exist_ok=True,
    )

    return backup_dir


def backup_certificate(source: Path, destination: Path) -> Path:
    """
    Backup a certificate file.

    Returns:
        Path to copied file.
    """
    if not destination.exists():
        print("Create folder destination")
        destination.mkdir(
            parents=True,
            exist_ok=True,
        )

    target = destination / source.name
    shutil.copy2(source, target)

    return target

