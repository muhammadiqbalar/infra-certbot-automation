import logging
import logging.config
from pathlib import Path

import yaml

def setup_logger() -> logging.Logger:
  """
  Configure application logging from YAML.
  """

  BASE_DIR = Path(__file__).resolve().parent.parent.parent
  config_path = BASE_DIR / "config" / "logging.yaml"
  
  with config_path.open("r", encoding="utf-8") as file:
      config = yaml.safe_load(file)
  
  logging.config.dictConfig(config)

  return logging.getLogger()
