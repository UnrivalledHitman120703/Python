# map() function
# Name = Indrajeet Mondal; Date = 5th October 2023
# SourceCode

def multiply_by_2(item):
    return item * 2


list1 = [10, 20, 30]
x = map(multiply_by_2, list1)
print(x)
y = list(x)
print(y)
