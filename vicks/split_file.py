
from itertools import zip_longest

def split(file = 'input/really_big_file.txt'):
    n = 3

    def grouper(n, iterable, fillvalue=None):
        args = [iter(iterable)] * n
        return zip_longest(fillvalue=fillvalue, *args)

    with open(file) as f:
        for i, g in enumerate(grouper(n, f, fillvalue=''), 1):
            with open(f'vicks/output/{i}.txt', 'w') as fout:
                fout.writelines(g)
