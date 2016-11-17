"""
+ sign is so called syntactic sugar - it calls __add__() method

e.g.

var1 = "Hello"
var2 = " World"

var1 + var2
is the same as
var1.__add__(var2)

"""


class SumList(object):
    def __init__(self, this_list):
        self.mylist = this_list

    def __add__(self, other):
        # list comprehension
        new_list = [x + y for x, y in zip(self.mylist, other.mylist)]
        return SumList(new_list)

    def __repr__(self):
        return str(self.mylist)

cc = SumList([1, 2, 3, 4, 5])
dd = SumList([100, 200, 300, 400, 500])

print(cc + dd)

