# reduce() function
# Name = Indrajeet Mondal; Date = 5th October 2023
# SourceCode

from functools import reduce

list1 = [1, 2, 3]


def mult_by_2(item):
    return item * 2


def only_odd(item):
    return item % 2 != 0


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(list1)
x = reduce(accumulator, list1, 0)
print(x)
