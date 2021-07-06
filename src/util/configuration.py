from pathlib import Path
from typing import MutableMapping
import toml

config = toml.load('./config.toml')
print(type(config))
print(config)

class Configuration():
    def __init__(self, config_file_path: str = './config.toml'):
        self.__config_file_path = config_file_path
        self.__config = toml.load(self.__config_file_path)

    def load(self, config_file_path: str):
        path = Path(config_file_path)
        if not path.exists():
            raise ValueError('File not found at {config_file_path}')
        self.__config_file_path = config_file_path
        self.__config = toml.load(self.__config_file_path)

    def get_config(self):
        return self.__config

    def get_config_file_path(self) -> str:
        return self.__config_file_path
    
    def get_project(self):
        return self.__config['project']
