import yaml

def load_config(yaml_string: str) -> dict:
    config = yaml.safe_load(yaml_string)
    if isinstance(config, dict):
        return config
    return {"data": config}
