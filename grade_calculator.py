#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    grades =[]
    while True:
        user_input = input("Enter your grades or type -1 to exit : ")
        if user_input == "-1":
            print(f" Your grades are : {grades}")
            print("\n  Thanks for using grade calculator \n Completed by : Krishnakumar AP")
            break
        else:
            grades.append(user_input)

            
if __name__ == "__main__":
    main()