from pathlib import Path
import shutil

from utils.logger import setup_logger
from utils.yaml_loader import load_yaml

from backup.helper import create_backup_directory
from backup.verify import verify_certificate_directory
from backup.metadata import write_backup_metadata
from backup.retention import deleted_old_backups
from models.backup import BackupResult

BASE_DIR = Path(__file__).resolve().parent.parent.parent
CONFIG_FILE = BASE_DIR / "config" / "config.yaml"

def backup_certificate(source: Path, destination: Path) -> None:
    """
    Copy certificate directory to backup location.
    """
    
    shutil.copytree(
      src=source,
      dst=destination,
      symlinks=False,
      dirs_exist_ok=True,
    )
logger = setup_logger()

def run_backup() -> None:
    """
    Backup all configure certificate.
    """

    config = load_yaml(CONFIG_FILE)

    backup_root = BASE_DIR / config["backup"]["directory"]
    
    backup_dir = create_backup_directory(backup_root)
  
    logger.info("Starting certificate backup")
    print("=" * 60)
    print("Certificate Backup")  
    print("=" * 60)
    print(f"Backup Directory : {backup_dir}")
    print()

    success = 0

    failed = 0

    results: list[BackupResult] = []

    for cert in config ["certificates"]:
        
        source = Path(cert["path"])
        
        destination = backup_dir / cert["name"]
  
        print("=" * 60)
  
        print(f"Checking : {cert['name']}")
  
        print("=" * 60)
 
        logger.info(f"[{cert['name']}] Checking source")

        valid, missing = verify_certificate_directory(source)

        if not valid:

           logger.error(f"[{cert['name']}] Missing files : {', '.join(missing)}")

           print(f"ERROR: Missing Files - {', '.join(missing)}")
           
           results.append(
             BackupResult(
               name= cert["name"],
               status= "FAILED"
             )
           )
         
           print()
  
           failed +=1
     
           continue

        try:

           backup_certificate(source, destination)

           relative_path = destination.relative_to(BASE_DIR)

           file_count = len(list(destination.glob("*")))

           logger.info(f"[{cert['name']}] Backup completed ({file_count}) files -> {relative_path}")

           print("Backup Successfully")
           
           results.append(
             BackupResult(
               name=cert["name"],
               status="SUCCESS"
             )

           )
  
           print()
       
           success += 1
  
        except Exception as err:
           logger.error(f"[{cert['name']}] {err}")
           print(f"ERROR: {err}")
           results.append(
             BackupResult(
               name=cert["name"],
               status="FAILED"
             )
           )
           print()
           failed +=1
        
    
    print("=" * 60)

    print("Backup Summary")

    print("=" * 60)

    
    print(f"Success  : {success}")
    print(f"Failed   : {failed}")
    print(f"Location : {backup_dir}")
    
    write_backup_metadata(
    
      backup_dir=backup_dir,
      Certificates=results,
      success=success,
      failed=failed,
    )
    deleted, kept = deleted_old_backups(
      backup_root=backup_root,
      retention=config["backup"]["retention"],
    )
    logger.info(
      f"Retention policy completed "
      f"(deleted={deleted}, kept={kept})"
    )

    logger.info(
      f"Backup Completed successfully"
      f"({success} success, {failed} failed)"
    )
         
 




