"""
Assignment 3

Read/Write config file via dictionary object.
"""
import os


class ConfigDict(dict):

    def __init__(self, config_file):
        self._config_file = config_file
        if os.path.isfile(self._config_file):
            with open(self._config_file) as file:
                for line in file:
                    line = line.rstrip()
                    key, value = line.split('=', 1)
                    dict.__setitem__(self, key, value)

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        with open(self._config_file, 'w') as file:
            for key, value in self.items():
                file.write("{key}={value}\n".format(key=key, value=self[key]))
