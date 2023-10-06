# Lambda expressions
# Name = Indrajeet Mondal; Date = 6th October 2023
# SourceCode

from functools import reduce

list1 = [1, 2, 3]

print('Multiply by 2:- ')
print(list1)
print(list(map(lambda item: item * 2, list1)))

print('Filter only odd numbers:- ')
print(list1)
print(list(filter(lambda item: item % 2 != 0, list1)))

print('Reduce with lambda:- ')
print(list1)
print(reduce(lambda acc, item: acc + item, list1))

# Some examples of lambda expression implementation

# Example 1: Square
list1 = [5, 4, 3]

new_list = list(map(lambda num: num ** 2, list1))
print(new_list)

# Example 2: List Sorting
a = [(0, 2), (4, 3), (10, -1), (9, 9)]
a.sort(key = lambda x: x[1])
print(a)
