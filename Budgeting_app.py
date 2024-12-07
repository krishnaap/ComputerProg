#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 01:00:30 2024

@author: krishna
"""
import locale as lc

lc.setlocale(lc.LC_ALL, 'en_US.UTF-8    ') # Ubuntu having issues without running UTF-8

def main():
    print("+++++++++ Welcome to Budget Tracker App +++++++++++") # Title
    total_income = income()
    exp = get_expenses()                                        # Copying expense list to display later
    total_expense = sum(exp)                                    # Finding the sum from the list of Expenses
    remaining_budget = total_income-total_expense
    print(("\nBudget Results:\n"))
    print(("----------------------------------\n"))
    print(f"Total Income: ${total_income:,.2f}\n")             # Diplaying the income
    print(f"Total Expenses: ${total_expense:,.2f}\n")          # Diplaying the total expenses 
    print(f"Remaining budget: ${remaining_budget:,.2f}")       # Diplaying the remaining balance 
    print("\n Complete Expense List")
    print("-----------------------------------------")
    n = len(exp)
    for i in range(0,n):
        print(f"{i+1}. {lc.currency(exp[i])}")                  # Diplaying the list of expenses one by one using currency symbol and formating from locale

def income():
    while True:
        income = input("Enter your total income : $ ")
        try:
            income_value = float(income)
            if income_value  < 0:
                print("Your input value is less than 0, please enter a valid income")
            else:
                return income_value
        except ValueError as e:
            print(f"Invalid input : could not convert string to float: {income}. Please enter a valid income amount.")
 
def get_expenses():
    expenses = []
    while True:
        expense_input = input("Enter an expense amount (or 0 to exit): $ ")
        if expense_input == '0':
            break
        try:
            expense_value = float(expense_input)
            if expense_value < 0:
                print("Invalid input: Expense cannot be negative. Please enter a valid expense amount or 0.")
            else:
                expenses.append(expense_value)
        except ValueError as e:
            print(f"Invalid input: could not convert string to float: '" + expense_input + "'. Please enter a valid expense amount or 0.")
    return expenses           
      
        
if __name__=='__main__':
    print("======================")
    print("Welcome to the Contact Manager App")
    main()    
    # print(f"Your total income is : $ {income_value}")
    print("Created by : Krishnakumar AP")
        