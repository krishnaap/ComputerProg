#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 11:55:56 2024

@author: krishna
"""
import datetime
def main():
    tasks =[]
    print("++ Welcome to Weekly Planner App ++")
    print("============================================")
    while True:
        print("1 - Add task")
        print("2 - View Tasks Due This Week") 
        print("3 - List All Scheduled Tasks")
        print("4 - Exit")
        print("============================================")
        inp = input("Select an option : ")
        print("============================================")
        
        if inp =='1':
            add_task(tasks)
        elif inp =='2':
            view_weekly()
        elif inp =='3':
            list_all()
        elif inp =='4':
            save_exit()
            break
        else:
            print("Enter a valid option ")

def add_task(tasks):
    while True:
        name_task =input("Enter the name of the task : ")
        date_inp = input("Enter Date in  YYYY-MM-DD format : ")        
        try:
            due_date=datetime.datetime.strptime(date_inp,"%Y-%m-%d")    
            tasks.append({'name_task':name_task,'due_date':due_date})
            print(f"Task {name_task} scheduled on {due_date.date()}")
            print("\n------------------------------------------")
            
            break
        except ValueError:
            print("Invalid date format, please follow the  'YYYY-MM-DD' format")
    
def view_weekly(tasks):
    print("============================================")
    print("Task due this week: ")
    print("\n------------------------------------------")
    today = datetime.datetime.today()
    start_week = today - datetime.timedelta(days=today.weekday())
    end_week = start_week + datetime.timedelta(days=6)
    found_task = False
    for name_task in tasks:
        if start_week <= name_task['due_date'] <= end_week:
            print(f"- {name_task['name']} due on {name_task['due_date'].date()}")
            found_task = True
    if not found_task:
        print("No tasks are due this week.")

def list_all(tasks):
    if not tasks:
        print("No tasks have been scheduled.")
    else:
        sorted_tasks = sorted(tasks, key=lambda x: x['due_date'])
        print("All scheduled tasks:")
        for task in sorted_tasks:
            print(f"- {tasks['name']} due on {tasks['due_date'].date()}")
            
def save_exit():
    print("Thanks for using our Weekly Planner App")

        
    
if __name__=='__main__':
    main()