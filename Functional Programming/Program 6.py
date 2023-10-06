# List Comprehensions
# Name = Indrajeet Mondal; Date = 6th October 2023
# SourceCode

# Various ways of using list comprehensions
# They
# make the code shorter at the cost of readability
my_list1 = [char for char in 'hello']
print('List 1:- ')
print(my_list1)

my_list2 = [num for num in range(0, 100)]
print('List 2:- ')
print(my_list2)

my_list3 = [num * 2 for num in range(0, 100)]
print('List 3:- ')
print(my_list3)

my_list4 = [num ** 2 for num in range(0, 100) if num % 2 == 0]
print('List 4:- ')
print(my_list4)
