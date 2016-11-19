# trapping and raising exceptions

def make_delim_line(list_to_join, delim):
    try:
        forward_line = delim.join(list_to_join)
    except TypeError:
        raise TypeError('make_delim_line(): arg 1 must be string')
    return forward_line


fline = make_delim_line('a', ',')

# exception attributes

mydict = {'a': 1, 'b': 2}

try:
    print(5 / 0)
except ZeroDivisionError as e:
    print(e)
    print(e.args)
