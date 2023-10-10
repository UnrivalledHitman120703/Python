# Using regex to check password
# Name = Indrajeet Mondal; Date = 11th October 2023
# SourceCode

import re

password = input("Enter password: ")
pattern = r"^(?=.*[@#$%^&+=])(?=.*[a-z])(?=.*[A-Z])(?=.{8,})"

if re.match(pattern, password):
    print("Valid password")
else:
    print("Invalid password")
