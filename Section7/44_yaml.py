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
