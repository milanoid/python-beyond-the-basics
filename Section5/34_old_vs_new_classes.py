"""
Guido's history of the development of Python
http://python-history.blogspot.com/2010/06/inside-story-on-new-style-classes.html
"""


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
