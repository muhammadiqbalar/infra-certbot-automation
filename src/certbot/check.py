from pathlib import Path


def check_certificate(cert_path: str):
     """
     Check whether the certifacte file exists.
     """

     cert_file = Path(cert_path)

     if not cert_file.exists():
         print("Error: Certificate file not found.")
         return False

     print("Certificate file found.")
     return True
