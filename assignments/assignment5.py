import os

import pickle


class ConfigKeyError(Exception):
    def __init__(self, config_dict, key):
        available_keys = [key for key in config_dict.keys()]
        self.message = "Key '{key}' not found. " \
                       "Available keys: {available_keys}".format(key=key, available_keys=available_keys)

    def __str__(self):
        return self.message


class ConfigDict(dict):
    config_directory = 'c:\\configs\\'

    def __init__(self, config_file):
        self._config_file = os.path.join(self.config_directory, config_file)
        if not os.path.isfile(self._config_file):
            try:
                file = open(self._config_file, mode='w')
                file.write("{}")
                file.close()
            except IOError:
                raise IOError('could not write file in path {path}'.format(path=self._config_file))

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

    def __getitem__(self, key):
        if key not in self:
            raise ConfigKeyError(self, key)
        return dict.__getitem__(self, key)


cd = ConfigDict(config_file='config.pickle')
cd['key1'] = 'value1'
