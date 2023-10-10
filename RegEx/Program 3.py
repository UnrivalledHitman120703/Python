# RegEx to check for email address
# Name = Indrajeet Mondal; Date = 11th October 2023
# SourceCode

# Importing the python module for implementing regex
import re

# Pattern to be checked
email_regex = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

# Declaring a string
email = "example1@example1.com"

# Some functions in regex
a = email_regex.search(email)
print(a)
b = email_regex.findall(email)
print(b)
c = email_regex.fullmatch(email)
print(c)
d = email_regex.match(email)
print(d)
