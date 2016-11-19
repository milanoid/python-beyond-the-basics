"""
Basic example
"""

import pickle

# mylist = ['a', 'b', 'c', 'd']
#
# with open('datafile.txt', 'wb') as fh:
#     pickle.dump(mylist, fh)
#
# with open('datafile.txt', 'rb') as fh:
#     unpickledlist = pickle.load(fh)
#
# print(unpickledlist)

"""
We can save entire instances too
"""


class MyClass(object):
    def __init__(self, init_val):
        self.val = init_val

    def increment(self):
        self.val += 1


cc = MyClass(5)
cc.increment()
cc.increment()

with open('datafile.txt', 'wb') as fh:
    pickle.dump(cc, fh)

with open('datafile.txt', encoding="utf-8") as fh:
    unpickled_cc = pickle.load(fh)

print(unpickled_cc)
print(unpickled_cc.val)
