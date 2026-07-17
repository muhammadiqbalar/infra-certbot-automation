from pathlib import Path
from utils.yaml_loader import load_yaml

config = load_yaml(Path("../config/config.yaml"))

print(config)
