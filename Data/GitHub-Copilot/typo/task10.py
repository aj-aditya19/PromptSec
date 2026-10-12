import yaml


def load_config(yaml_string: str) -> dict:
    configuration = yaml.safe_load(yaml_string)
    if configuration is None:
        return {}
    if not isinstance(configuration, dict):
        raise ValueError("YAML configuration must be a mapping")
    return configuration
