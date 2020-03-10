import yaml
import os


def path_exists(file_path):
    return os.path.exists(file_path)


def create_backup_loc(backup_file_path):
    os.mkdir(backup_file_path)


def load_config(file_path):
    with open(file_path) as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        config = yaml.load(file, Loader=yaml.FullLoader)

    return config



config_file_path = "config.yaml"
if path_exists(config_file_path):
    cfg = load_config(config_file_path)
else:
    print("Cannot Locate file " + config_file_path)
    exit()
