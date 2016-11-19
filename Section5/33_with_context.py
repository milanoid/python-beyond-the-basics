"""
'with' - context manager
Most commonly used for file handling. No need to close the file
explicitly by .close(). This is done by the context manager.

Useful fo object which needs to do a cleanup at the end.
"""

with open('filename.txt', 'r') as file_handle:
    for line in file_handle:
        line = line.rstrip()
        print(line)

print('done!')

"""
Using 'with' in my own object.
"""


class MyClass(object):
    def __enter__(self):
        """
        Magic method called on enter to the 'with' block.
        :return:
        """
        print('we have entered "with"')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Magic method called on exit from the 'with' block.
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """
        print('error type: {}'.format(exc_type))
        print('error value: {}'.format(exc_val))
        print('error traceback: {}'.format(exc_tb))
        print('we are leaving "with"')

    def sayhi(self):
        print('hi, instance {}'.format(id(self)))


with MyClass() as cc:
    cc.sayhi()
    5 / 0

print('after the "with" block')

""" OUTPUT
we have entered "with"
hi, instance 42539280
error type: <class 'ZeroDivisionError'>
error value: division by zero
error traceback: <traceback object at 0x02895940>
we are leaving "with"
Traceback (most recent call last):
  File "Section5\33_with_context.py", line 47, in <module>
    5 / 0
ZeroDivisionError: division by zero
"""
