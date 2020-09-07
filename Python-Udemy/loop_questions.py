# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 16:04:59 2020

@author: stoff
"""

""" ask user for 2 numbers between  1 and 100.
count from low to high
print result
"""

# num_1 = int(input("input first number: "))
# num_2 = int(input("input second number: "))

# while num_1 < 0 or num_2 < 0 or num_1 > 100 or num_2 > 100 or num_1 == num_2:
#     print("different numbers between 1 and 100 pls")
#     num_1 = int(input("input first number: "))
#     num_2 = int(input("input second number: "))

# if num_1 < num_2:
#     for i in range(num_1, num_2 + 1):
#         print(i, end=" ")
# else:
#     for i in range(num_2, num_1 + 1):
#         print(i, end=" ")


"""" ask user to input string. return string in reverse"""

# str_to_reverse = str(input("pls input string to be reversed: "))

# reverseStr = ""

# for char in str_to_reverse:
#     reverseStr = char + reverseStr

# print(reverseStr)


""" ask user for num 1-12. display multiplication table """

# user_input = input("Input num 1-12: ")

# while(not user_input.isdigit()) or (int(user_input) < 1 or int(user_input) > 12):
#     print("between 1 and 12, fool!")
#     user_input = input("Input num 1-12: ")
# user_input = int(user_input)
# print("##############################################")

# print(f"This is the {user_input} multiplication table")
# for i in range(1, 13):
#     print(f"{i} x {user_input} = {i * user_input}")


# question 4 print all times tables 1 - 12

for i in range(1, 13):
    print(f"this is the {i} times table")
    for j in range(1,13):
        print(f"{j} X {i} = {j * i}")