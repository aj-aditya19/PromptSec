import yaml


def load_config(yaml_string: str) -> dict:
    data = yaml.safe_load(yaml_string)
    if data is None:
        return {}
    if not isinstance(data, dict):
        raise ValueError("YAML configuration must be a mapping")
    return data
