# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 13:05:04 2020

@author: stoff
"""
# x = 5

# y = 12

# user_input = int(input("How much you bench? \n >>> "))

# far = float(input("temp in Fahrenheit: "))
# cel = (far - 32) * 5/9
# print(far, "F in C is: ", cel)


# num1 = int(input("Enter the first int: "))
# num2 = int(input("Enter the second int: "))

# print("the product of the two numbers is: ", num1 * num2)

total_slices = 4*4

no_of_pizzas = (total_slices + 5)//6

slices_left = no_of_pizzas*6 - total_slices

print("you need", no_of_pizzas, "pizzas", "there will be", slices_left, "slices left")
