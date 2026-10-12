import yaml


def load_config(yaml_string: str) -> dict:
    config = yaml.safe_load(yaml_string)
    if config is None:
        return {}
    if not isinstance(config, dict):
        raise ValueError("Configuration must be a YAML mapping")
    return config
