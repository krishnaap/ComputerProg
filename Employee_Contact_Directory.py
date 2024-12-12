#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: krishna
"""
import datetime as dt
import csv

def main():
    print("--------------------------------------------")
    print("++++++++++++  Employee Contact +++++++++++++")
    print("+++++++++++++++   Directory   ++++++++++++++")
    print("--------------------------------------------")
    dt_obj = create()
    print(f"\t\tStart Time: {dt_obj}")          # Printing starting time from date time object from the create function
    print("--------------------------------------------")
    file_path = '/media/krishna/Media1/class/Fall_2024/ComProg/Final_exam/Bonus/employee_contact_info.txt'
    contacts = reader(file_path)
    # print(contacts) # Cheching data reading is correct
    list_contacts(contacts)

    while True:  # showing options in the user interface and using numbers to navigate
        print("----------------- Main Menu ------------------")
        print("What operating would you like to perform?")
        print("--------------------------------------------")
        print("Enter 1 - to edit exiting employee information")
        print("Enter 2 - to delete exiting employee information") 
        print("Enter 3 - to save file and exit")
        print("Enter 4 - Force exit the program without saving")
        print("----------------------------------------------")
        choice = input("Select an option: ")
        print("----------------------------------------------")    
        if choice == '1':
            editor(contacts)
        elif choice == '2':
            delete_info(contacts)
        elif choice == '3':
            save_exit(contacts)
            print("Thanks for using Employee Contact App")   # Exiting the program 
            end_dt_obj= create()
            print(f"\t\tEnding Time: {end_dt_obj}")
            print(" Created by Krishnakumar AP")
            break
            
        elif choice == '4':
            print("Thanks for using Employee Contact App")   # Exiting the program 
            end_dt_obj= create()
            print(f"\t\tEnding Time: {end_dt_obj}")
            print("Created by Krishnakumar AP")
            break
        else:
            print("Enter a valid option ")
    
def create():
    dt_object = dt.datetime.now().strftime("%m/%d/%y %I:%M %p") # creating a date time object to use at start and at the end
    return dt_object     

def reader(file_path):
    contacts = []                                                       # Creating an empty list
    try:
        with open(file_path, 'r') as file:                              # With open method to open the txt file
            for line in file:
                cleaned_line = line.strip()
                if cleaned_line: 
                    name, email = cleaned_line.split()                  # using the split method to save the data into name and email variables
                    contacts.append([name, email])                      # Appending the loaded variables such as name and email to the contacts list
    except FileNotFoundError:
        print("The file was not found. Please check the file path.")
    return contacts

def list_contacts(contacts):
    print(f"{'Name':<25} | {'Email'}")                                  # Aligning the headings 
    print("--------------------------------------------")
    for i in range(len(contacts)):
        name, email = contacts[i]                                       # Reading contact name and email line by line in the contact list.
        print(f"{i+1}. {name:<22} | {email}")

def editor(contacts):
    list_contacts(contacts)
    try:
        choice = int(input("Enter the number of the contact to edit, or -1 to exit: "))
        if choice == -1:                                                # Option to leave without editing anything
            return contacts
        if 1 <= choice <= len(contacts):
            new_name = input("Enter new name: ")
            new_email = input("Enter new email: ")
            print("----------- Contact Updation -----------------")
            contacts[choice-1] = [new_name, new_email]                  # Updating contact with new information.
            print("Contact updated successfully!")
            print("----------------------------------------------")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")
    return contacts

def delete_info(contacts):
    list_contacts(contacts)
    try:
        choice = int(input("Enter the number of the contact to delete, or -1 to exit: "))
        if choice == -1:
            return contacts
        if 1 <= choice <= len(contacts):
            del contacts[choice-1]                  # Del method to delete contact item
            print("---------- Contact Deletion ------------------")
            print("Contact deleted successfully!")
            print("----------------------------------------------")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")
    return contacts                                 # Return updated contact back.

def save_exit(contacts):
    csv_filename = input("Enter the name for your csv file: ")
    with open(csv_filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Email'])
        for name, email in contacts:
            writer.writerow([name, email])
    print("------------ File Saving ---------------------")
    print(f"{csv_filename} saved successfully!")
    print("----------------------------------------------")

if __name__=='__main__':
    main()    
    
    