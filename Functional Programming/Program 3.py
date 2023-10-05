# zip() function
# Name = Indrajeet Mondal; Date = 5th October 2023
# SourceCode

list1 = [1, 2, 3]
list2 = [10, 20, 30]

print(list1)
print(list2)

x1 = zip(list1, list2)
print(x1)
y1 = list(x1)
print(y1)

x2 = zip(list2, list1)
print(x2)
y2 = list(x2)
print(y2)
