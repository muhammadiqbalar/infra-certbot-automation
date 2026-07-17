from pathlib import Path
import yaml



def load_yaml(config_path: Path) -> dict:
    """
    Loader Yaml Configuration file.

    Args:
        config_path: Path to YAML file.

    Returns:
       Dictionary containing configuration.
    """
    if not config_path.exists():
       raise FileNotFoundError(
           f"Configuration file not found: {config_path}"
       )
    with config_path.open("r", encoding="utf-8") as file:
       return yaml.safe_load(file)
