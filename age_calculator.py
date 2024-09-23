#!/usr/bin/env python3
# -*- coding: utf-8 -*-

first_name = input("Enter your first name: ") # User input for first name

last_name = input("Enter your last name: ") # User input for last name


current_year = int(input("Enter the current year: "))


birth_year = int(input("Enter your birth year: "))


age = current_year - birth_year

print("Hello, " + first_name + " " + last_name + "!\n" + "You are " + str(age) + " years old this year.")


age += 1


print(f"Next year, you will be {age} years old.")


print("Completed by, Krishnakumar AP")

#%%
print(3==5)

print("Apple">"Apple")

print("10"<"5")