# filter() function
# Name = Indrajeet Mondal; Date = 5th October 2023
# SourceCode
def check_odd(item):
    return item % 2 != 0


list1 = [1, 2, 3]
print(list1)
x = filter(check_odd, list1)
print(x)
y = list(x)
print(y)
