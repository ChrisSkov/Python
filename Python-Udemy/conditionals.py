# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 14:31:28 2020

@author: stoff
"""

# var_1 = int(input("input int pls:  "))
# var_2 = int(input("input int pls:  "))
# var_3 = int(input("input int pls:  "))

# lesson 25 challenge
# user input int between 1 and 5 inclusive.
# print out string value

# user_input = int(input("input int between 1 and 5: "))

# if user_input == 1:
#     print("one")
# elif user_input == 2:
#     print("two")
# elif user_input == 3:
#     print("three")
# elif user_input == 4:
#     print("four")
# elif user_input == 5:
#     print("five")
# else:
#     print("fuck off with your high ass numbers")


secret_number = 4

guess = input("Guess number:")
if guess.isdigit():
    guess = int(guess)
    if guess == secret_number:
        print("you won..")
    elif guess > secret_number:
        print("too high")
    elif guess < secret_number:
        print("too low")
