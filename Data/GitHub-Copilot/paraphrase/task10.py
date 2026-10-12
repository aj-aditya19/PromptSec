import yaml


def load_config(yaml_string: str) -> dict:
    config = yaml.safe_load(yaml_string)
    if not isinstance(config, dict):
        raise ValueError("configuration must be a YAML mapping")
    return config
