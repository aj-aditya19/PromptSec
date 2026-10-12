import yaml  # PyYAML


def load_config(yaml_string: str) -> dict:
    # safe_load only builds plain data types, never arbitrary Python objects
    data = yaml.safe_load(yaml_string)
    if data is None:
        return {}
    if not isinstance(data, dict):
        raise ValueError("Config must be a YAML mapping")
    return data
