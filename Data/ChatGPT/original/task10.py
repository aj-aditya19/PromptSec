import yaml

def load_config(yaml_string: str) -> dict:
    """Load YAML settings using safe_load to avoid constructing arbitrary objects."""
    result = yaml.safe_load(yaml_string)
    if result is None:
        return {}
    if not isinstance(result, dict):
        raise ValueError("YAML configuration must be a mapping")
    return result
