# old style "Classic" class
class OldClass():
    pass


# new style class (since Python 2.2)
class NewClass(object):
    pass


oc = OldClass()
nc = NewClass()

print(type(oc))
print(type(nc))

print
oc.__class__
