"""
PDB Python Debugger

c - continue
q - quit debugging
n - next line (step over?)
s - step (into)
list - see the code and position
h - help
"""

import pdb

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for val in values:
    mysum = 0  # bug
    mysum = mysum + val
    pdb.set_trace()  # break point, type c to continue

print(mysum)
