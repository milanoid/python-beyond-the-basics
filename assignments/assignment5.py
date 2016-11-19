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
        self._config_file = os.path.join(ConfigDict.config_directory, config_file + '.pickle')
        if not os.path.isfile(self._config_file):
            with open(self._config_file, 'wb') as fh:
                pickle.dump({}, fh)

        with open(self._config_file, 'rb') as fh:
            pkl = pickle.load(fh)
            self.update(pkl)

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        with open(self._config_file, 'wb') as fh:
            pickle.dump(dict, fh)

    def __getitem__(self, key):
        if key not in self:
            raise ConfigKeyError(self, key)
        return dict.__getitem__(self, key)


cd = ConfigDict(config_file='test')
cd['key1'] = 'value1'

print(cd)
