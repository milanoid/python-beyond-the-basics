"""
 Usages:
    ./run_assignment3.py                        (reads out hte entire config dict)
    ./run_assignment3.py thiskey this value     (sets 'thiskey' and 'thisvalue' in the dict)
"""

import sys
from assignments.assignment3 import ConfigDict

cd = ConfigDict('config_file.txt')

if len(sys.argv) == 3:
    key = sys.argv[1]
    value = sys.argv[2]
    print('writing data {key} {value}'.format(key=key, value=value))

else:
    print('reading data')
    for key in cd.keys():
        print(' {key} = {value}'.format(key=key, value=cd[key]))

cd['secret_password'] = '^$#&^&'
cd['username'] = 'milanoid'
cd['password'] = 'secret'
cd['hosntame'] = 'localhost'
cd['port'] = 'port'