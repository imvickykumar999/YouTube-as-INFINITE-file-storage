
from itertools import zip_longest
import os

n = 2
file = 'input/really_big_file.txt'

try:
    os.mkdir('output')
except Exception as e:
    pass

def grouper(n, iterable, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)

with open(file) as f:
    for i, g in enumerate(grouper(n, f, fillvalue=''), 1):
        with open(f'output/{i}.txt', 'w') as fout:
            fout.writelines(g)
