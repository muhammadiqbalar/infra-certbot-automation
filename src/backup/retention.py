from pathlib import Path
import shutil


from utils.logger import setup_logger

BASE_DIR = Path(__file__).resolve().parent.parent.parent

logger = setup_logger()

def deleted_old_backups(backup_root: Path, retention: int) -> None:
    """
    Keep only the newest 'retention backup directory'.
    """

    backups = sorted(
        [
           item
           for item in backup_root.iterdir()
           if item.is_dir()
        ]
    )
    
    if len(backups) <= retention:
        logger.info(
            f"No old backup to delete"
            f"(current={len(backups)}, retention={retention})"
        )

        return 0, len(backups)

    old_backups = backups[:-retention]
    
    deleted = 0

    for backup in old_backups:
        shutil.rmtree(backup)
    
        relative_path = backup.relative_to(BASE_DIR)

        logger.info(
           f"Deleted old backup -> {relative_path}"
        )
        deleted +=1
    kept = retention
    return deleted, kept
