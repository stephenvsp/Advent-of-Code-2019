# found on /r/advent_of_code needed help with solution
# https://github.com/gboyegadada/algos/blob/master/AoC19/day14.py

import sys
from math import ceil

f = sys.argv[1]


def dictint(x): return (x[1], int(x[0]))


def pairs(s): return dict(dictint(x.split(' ')) for x in s.split(', '))


data = [pairs(x) for l in open(f) for x in l.strip().split(' => ')]

reactants, elements = [], []

for i in range(0, len(data), 2):
    # right list is dervied element AB
    # left list is elements used to make A, B => AB

    reactants.append(data[i])
    elements.append(data[i+1])


def quantity(element: str = 'ORE', fuel=1):
    if element == 'FUEL':
        return fuel

    q = 0

    for i, recipe in enumerate(reactants):
        if element in recipe:

            parent, *_ = list(elements[i])
            parent_batch_quantity = elements[i][parent]

            q += ceil(quantity(parent, fuel) /
                      parent_batch_quantity) * recipe[element]

    return q


print(quantity('ORE', 1))
