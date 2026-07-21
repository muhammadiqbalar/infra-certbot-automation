from pathlib import Path

from backup.backup import create_backup_directory, backup_certificate


backup_roots = Path("backups")
backup_dir = create_backup_directory(backup_roots)


domains =  [
   Path("certs/prod/fullchain.pem"),
   Path("certs/dev/fullchain.pem"),
]


for source in domains:
   print(f"Backup {source}")

   backup_certificate(
     source, 
     backup_dir,
   )
   
   print("Backup Finished")

