import yaml

def load_config(yaml_string: str) -> dict:
    return yaml.safe_load(yaml_string) or {}
