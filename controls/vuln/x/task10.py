import yaml
def load_config(yaml_string): return yaml.load(yaml_string, Loader=yaml.Loader)
