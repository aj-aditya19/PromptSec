import yaml

def load_config(yaml_string: str) -> dict:
    """Load YAML using PyYAML's safe loader."""
    value = yaml.safe_load(yaml_string)
    if value is None:
        return {}
    if not isinstance(value, dict):
        raise ValueError("YAML configuration must be a mapping")
    return value
