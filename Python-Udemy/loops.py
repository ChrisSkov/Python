# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 13:36:46 2020

@author: stoff
"""
# range(10) 0-9
# for i in range(10):
#     print(i)

# range(start number, end number - 1)
# for i in range(1, 11):
#     print(i, end=" ")


# Lists

data = [23, 25, 66, 100, 92]

# for num in data:
#     print(num, end=" ")

# count = 0
# for num in data:
#     count += num

# print(count)
# Bubble sort
# data_copy = data[:]
# for i in range(len(data_copy)):
#     for j in range(0, len(data_copy)-i-1):
#         if data_copy[j] > data_copy[j + 1]:
#             data_copy[j], data_copy[j + 1] = data_copy[j + 1], data_copy[j]
# print(data_copy)

# print(sorted(data_copy))


# count = 0
# class_names = []
# name = input("Enter name type n to stop:> ")
# while name != "n":
#     count += 1
#     class_names.append(name)
#     print(f"{name} has been added.")
#     name = input("Next name? :> ")

# print(f"there are {count} people in this data structure. they are {class_names}")

# Modulus
var_1 = 20
var_2 = 4

# FizzBuzz

n = 100
for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print(i, "FizzBuzz")
    elif i % 5 == 0:
        print(i, "Buzz")
    elif i % 3 == 0:
        print(i, "Fizz")
    else:
        print(i)
