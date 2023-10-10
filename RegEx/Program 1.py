# Introduction to RegEx
# Name = Indrajeet Mondal; Date = 11th October 2023
# SourceCode

# Importing the python module for implementing regex
import re

# Pattern to be checked
pattern = re.compile('this')
# Declaring a string
string = 'Search inside this text this'

# Some functions in regex
x = pattern.search(string)
print(x)
y = pattern.findall(string)
print(y)
z = pattern.fullmatch('this')
print(z)
w = pattern.match('this')
print(w)
