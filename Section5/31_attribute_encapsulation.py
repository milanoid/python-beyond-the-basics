"""
Attribute encapsulation via classic getter/setter paradigm

- very un-pythonic
"""


class MyClass(object):
    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value


a = MyClass()
b = MyClass()

a.set_value(10)
b.set_value(100)

print(a.get_value())
print(b.get_value())

"""
better way using @property decorator
"""


class GetSet(object):
    def __init__(self, value):
        self.attrval = value

        @property
        def var(self):
            print("getting the 'var' attribute")
            return self.attrval

        @var.setter
        def var(self, value):
            print("setting the 'var' attribute")
            self.attrval = value

        @var.deleter
        def var(self):
            print("deleting the 'var' attribute")
            self.attrval = None


me = GetSet(5)

me.var = 1000
print(me.var)
# causes AttributeError: 'GetSet' object has no attribute 'var'
# Python2 vs Python3
del me.var
print(me.var)
