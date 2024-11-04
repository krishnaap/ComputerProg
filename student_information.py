#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 21:13:32 2024

@author: krishna
"""
def main():
    student_info = {}                                                   # Made an empty dictionary to store student information

    student_info["Abby"] = {"ID": "1", "GPA": 3.8, "Credits-completed": 90, "Grades": [80,50,100,98]} # Student info 1
    student_info["Caleb"] = {"ID": "3", "GPA": 3.2, "Credits-completed": 60, "Grades": [50,80,80]}    # Student info 2
    print("Student Information Dictionary:")
    print(student_info)
    
    print("\n List of Students:\n")
    for name in student_info:
        print(name)
    print()                                                             # Creating a space between next output
    
    print("Accessing Student Information:")
    print("Name\t\tID\tGPA\tCredits-completed\tGrades")
    for name, info in student_info.items():                                     # Loop over items in the dictionary
        print(f"{name}\t{info['ID']}\t{info['GPA']}\t{info['Credits-completed']}\t{info['Grades']}")
    
    print("\n Caleb has dropped out, removing from student info registry")
    removed_student = student_info.pop("Caleb")                         # Removing 1 student from the dictionary by name
    print("Updated Student Information Dictionary:")
    print(student_info)
    print()

    print("Accessing GPA Information:")
    for name in student_info:
        gpa = student_info.get(name, {}).get("GPA", "N/A")
        print(f"{name}'s GPA: {gpa}")                                   # Displaying remaining student information by name and GPA
    print()


    print("Clearing Student Registry:")
    student_info.clear()
    print("Cleared Student Information Dictionary:")
    print(student_info)
    
    Name = "Krishnakumar AP"
    print(f"\n Completed by, {Name}")

if __name__ == "__main__":
    main()
