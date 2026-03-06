import yaml

with open('compose.yaml', 'r') as file:
    compose_file_setting = yaml.load(file, Loader=yaml.SafeLoader)

