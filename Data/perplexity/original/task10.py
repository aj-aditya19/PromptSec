import yaml

def load_config(yaml_string: str) -> dict:
    data = yaml.safe_load(yaml_string)
    return data if isinstance(data, dict) else {}
