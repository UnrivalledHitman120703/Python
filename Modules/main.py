# Implementing modules
# Name = Indrajeet Mondal; Date = 15th October 2023
# SourceCode

import shopping.shopping_cart as cart
import utility


if __name__ == "__main--":
    print("Using utility.divide() present in utility.py:- ", utility.divide(8, 4))
    print("Using utility.multiply() present in utility.py:- ", utility.multiply(2, 4))
    print("Using buy_item() from shopping.shopping_cart: ")
    print(cart.buy_item("Apple"))
