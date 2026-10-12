import yaml

def load_config(yaml_string: str) -> dict:
    """Load a YAML mapping safely as a dictionary."""
    result = yaml.safe_load(yaml_string)
    if result is None:
        return {}
    if not isinstance(result, dict):
        raise ValueError("YAML configuration must be a mapping")
    return result
