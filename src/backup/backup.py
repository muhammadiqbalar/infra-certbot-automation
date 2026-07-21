from pathlib import Path
import shutil

from utils.logger import setup_logger
from utils.yaml_loader import load_yaml

from backup.helper import create_backup_directory
from backup.verify import verify_certificate_directory


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

    for cert in config ["certificates"]:
        
        source = Path(cert["path"])
        
        destination = backup_dir / cert["name"]
  
        print("=" * 60)
  
        print(f"Checking : {cert['name']}")
  
        print("=" * 60)
 
        logger.info(f"[{cert['name']}] Checking source")

        valid, missing = verify_certificate_directory(source)

        if not valid:

           logger.info(f"[{cert['name']}] Missing files : {', '.join(missing)}")

           print(f"ERROR: Missing Files - {', '.join(missing)}")
         
           print()
  
           failed +=1
     
           continue
        try:
           backup_certificate(source, destination)
        
           logger.info(f"[{cert['name']}] Backup completed")

           print("Backup Successfully")
  
           print()
       
           success += 1
  
        except Exception as err:
           logger.error(f"[{cert['name']}] {err}")
           print(f"ERROR: {err}")
           print()
           failed +=1

    print("=" * 60)

    print("Backup Summary")

    print("=" * 60)

    
    print(f"Success  : {success}")
    print(f"Failed   : {failed}")
    print(f"Location : {backup_dir}")

    logger.info("Certificate backup Completed")
         
 




