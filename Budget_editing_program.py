#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: krishna
"""

import datetime
import csv

def main():
    print("++ Budget Editing Program ++")
    print("Start Time:", datetime.datetime.now().strftime("%m/%d/%y %I:%M %p"))
    
    print("============================================")
    file = '/media/krishna/Media1/class/Fall_2024/ComProg/Final_exam/exam_3_test_file.txt'
    budget_data = csv_reader(file)
    list_content(budget_data) # Displaying the imported data.
    print("What operating would you like to perform?")
    print("----------------------------------------------") 
    while True:  # showing options in the user interface and using numbers to navigate
        print("Enter 1 - to edit")
        print("Enter 2 - to delete a value") 
        print("Enter 3 - to write data to csv and close program")
        print("Enter -1 - to close program without operating")
        print("----------------------------------------------")
        choice = input("Select an option: ")
        print("----------------------------------------------")    
        if choice == '1':
            editor(budget_data)
        elif choice == '2':
            delete_val(budget_data)
        elif choice == '3':
            csv_writer(budget_data)
        elif choice == '-1':
            print("Thanks for using Budget Editing App")   # Exiting the program 
            break
        else:
            print("Enter a valid option ")
    
    
    print("============================================")
    print("End Time:", datetime.datetime.now().strftime("%m/%d/%y %I:%M %p"))
    print("Written by Krishnakumar AP")

# def csv_reader(file):
#     with open(file, 'r') as file:
#         lines = file.readline() # Using readline function to read every lines of the file
#         data = [line.strip().split('|') for line in lines]
#     return data # returning the content of the file

def csv_reader(file):
    data=[]
    with open(file, 'r') as file:
        for line in file:
            stripped_lines = line.strip()
            if stripped_lines:
                data.append(stripped_lines.split('|'))
                #print(data) # Debugging logical errors within the code to understand better
        
    return data


def list_content(data):
    print(f"{'Month'} \t|\t {'Amount'}")
    print("------------------------------")
    for item in data:
        print(f"{item[0]} \t\t {item[1]}")

def editor(data):
    print("Which value would you like to edit?")                                    
    for i in range(len(data)):
        print(f"{i+1}. {data[i][0]}:    {data[i][1]}")          # DIsplay with index to show items to delete

    try:
        choice = input("Enter the value to edit, or -1 to close: ").strip()
        if choice == '-1':
            print("No changes made.")
            return
        i = int(choice) - 1
        if i < 0 or i >= len(data):
            print("Invalid choice.")
            return
        current_month, current_amount = data[i]
        print(f"{current_month} Current value: {current_amount}")
        new_val = input("Enter the new value: ").strip()
        if new_val:
            data[i][1] = new_val
            print("Value updated.")
        else:
            print("No changes made.")
    except ValueError:
        print("Invalid input. No changes made.")    
    
    
def delete_val(data):
    print("Which value would you like to delete?")
    for i in range(len(data)):
        print(f"{i+1}. {data[i][0]}:    {data[i][1]}")          

    try:
        choice = input("Enter the value to delete, or -1 to close: ").strip()
        if choice == '-1':
            print("No changes made.")
            return
        i = int(choice) - 1
        if idx < 0 or i >= len(data):
            print("Invalid choice.")
            return
        to_remove = data[i]
        print(f"Removing {to_remove[0]} Value: {to_remove[1]}")
        del data[i]
    except ValueError:
        print("Invalid input. No changes made.")    


def csv_writer(data):
    print("------------------------------")
    csv_filename = input("Enter the name for your csv file: ")
    with open(csv_filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Month', 'Amount'])
        for item in data:
            writer.writerow(item) # Using writerow to save

if __name__ == '__main__':
    main()
