# CodeMetric Python Programming Internship
# Task 3
# Design a To-Do List Manager
# Build a console-based task manager that saves tasks persistently.
import json

TASKS_FILE = "tasks.json"


def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_tasks():
    with open(TASKS_FILE, "w") as file:
        json.dump(task_list,file,indent=4)


task_list = load_tasks()

def create_new():
    id = int(input("Enter The Task ID: "))
    title = input("Enter The Task Title: ")
    description = input("Enter The Task Description: ")
    task_dic = {"id": id, "title": title, "description": description}
    task_list.append(task_dic)
    save_tasks()
    print("Task Added!")

def delete_task():
    id = int(input("Enter The Task ID: "))
    for i in task_list:
        if i["id"] == id:
            task_list.remove(i)
            save_tasks()
            print("Deleted!")
            return
    print("Task ID not found.")

def show_list():
    if task_list:
        print("Current Tasks:")
        for task in task_list:
            print(f'ID: {task["id"]}, Title: {task["title"]}, Description: {task["description"]}')
    else:
        print("No tasks available.")

while True:
    print("\nTO DO LIST MANAGER")
    print("1: Create New Task")
    print("2: Delete A Task")
    print("3: Show List of Tasks")
    print("4: Exit")
    
    type_input = int(input("Enter your choice: "))
    
    if type_input == 1:
        create_new()
    elif type_input == 2:
        delete_task()
    elif type_input == 3:
        show_list()
    elif type_input == 4:
        print("Good Bye!")
        break
    else:
        print("Invalid choice, please try again.")