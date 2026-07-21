import json
import socket
from datetime import datetime
from pathlib import Path

def write_backup_metadata(backup_dir: Path, Certificates: list[dict], success: int, failed: int,) -> None:
    """
    Write backup metadata to backup_info.json
    """

    metadata = {
       "backup_id": backup_dir.name,
       "created_at": datetime.now().isoformat(timespec="seconds"),
       "hostname": socket.gethostname(),
       "total": len(Certificates),
       "success": success,
       "failed": failed,
       "certificates": Certificates,
    }

    output_file = backup_dir / "backup_info.json"

    with output_file.open(
       "w",
       encoding="utf-8"
    )as fp:
       json.dump(
         metadata,
         fp,
         indent=4
       )
