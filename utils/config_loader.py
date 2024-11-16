import yaml

def load_config(path='config/settings.yaml'):
    with open(path, 'r') as file:
        config = yaml.safe_load(file)
    return config

CONFIG = load_config()
