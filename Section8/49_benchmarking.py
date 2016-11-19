"""
Benchmarking - comparing two code snippets to see which executes faster

can be run straight from command line too:
python -m timeit -n 1000000 -s "mydict = {'a': 5, 'b': 6, 'c': 7}" "mydict.get('c')

"""

import timeit

print('by index: ', timeit.timeit(stmt="mydict['c']", setup="mydict = {'a': 5, 'b': 6, 'c': 7}", number=100000))

print('by get: ', timeit.timeit(stmt="mydict.get('c')", setup="mydict = {'a': 5, 'b': 6, 'c': 7}", number=100000))
