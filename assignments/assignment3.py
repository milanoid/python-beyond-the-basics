"""
Assignment 3

In this assignment we're going to leverage the convenience of a dictionary
to power a configuration file, which is simply a file of key-value pairs.
A configuration file is used quite often in programming shops to hold values
that don't belong in the Python script itself. Values like SQL queries,
email addresses, and other configurable values should be stored outside of the script,
because they may change when the code itself doesn't need to be changed.
The structure of a config file could take many forms, and one of them is a simple key=value syntax, with one key/value
pair per line.  This is simple and straightforward, so we'll use it.
What's great about using a built-in structure like a dictionary as the interface
to the configuration file is that any Python programmer will immediately know how to use it.
The instructions are so simple you almost don't need documentation:  "create a new ConfigDict object,
then read and write keys and values as desired" -- that's it.
"""


class ConfigDict(dict):
    _config_file = ''

    def __init__(self, config_file):
        self._config_file = config_file
        with open(self._config_file) as file:
            for line in file:
                key, value = line.split('=', 1)
                dict.__setitem__(self, key, value)

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        with open(self._config_file, 'w') as file:
            for key in self.keys():
                file.write("{key}={value}\n".format(key=key, value=self[key]))
        file.close()
