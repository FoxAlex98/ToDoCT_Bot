import yaml

with open('conf/settings.yaml') as yaml_conf:
    config_map = yaml.safe_load(yaml_conf)

TOKEN = config_map["token"]
