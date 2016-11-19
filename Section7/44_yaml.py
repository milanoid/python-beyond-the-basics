"""
YAML: "Yaml ain't markup language"
"""

import yaml
import json

mylist = [1, 2, 3, 4, 5]

loaded_yaml = yaml.dump(mylist, default_flow_style=False)
print(loaded_yaml)

with open('my.yaml') as fh:
    struct = yaml.load(fh)

print(json.dumps(struct, indent=4, separators=(',', ': ')))

"""
 storing class instance, the class code must available when calling load()
"""


class MyClass(object):
    classvar = 10

    def __init__(self, val):
        self.val = val

    def increment(self):
        self.val += 1

x = MyClass(5)
x.increment()
x.increment()

with open('obj.yaml', 'w') as fh:
    yaml.dump(x, fh)

with open('obj.yaml') as fh:
    inst = yaml.load(fh)

print(inst.val)