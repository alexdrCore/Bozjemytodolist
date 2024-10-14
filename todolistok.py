import json
from collections import deque

def load_tasks(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"{filename} is not found. New file will be created when you add your first task")
        return deque()
def add_task (tasks):
    while True:
        print("\nPrint /close to exit")
        task_input = input("Write your task : ")
        if check_for_close(task_input):
            break
        if task_input.strip():
            tasks.append({'task':task_input, 'completed':False})
            print(f"Task '{task_input}' is successfully added!\n")
            break
        else:
            print("Task can't be empty")
def update_task(tasks):
    pass
def delete_task (tasks):
    while True:
        get_tasks(tasks)
        print("Print /close to exit")
        index_for_delete = input("Write index of task to delete : ")
        if check_for_close(index_for_delete):
            break
        index_for_delete = is_valid_index(index_for_delete, tasks)
        if index_for_delete == None:
            continue
        while True:
            user_acceptance = confirm_action(input(f"Delete {index_for_delete+1}. {tasks[index_for_delete]['task']} ? Y/N : ").strip().lower())
            if user_acceptance:
                removed_task = tasks.pop(index_for_delete)
                print(f"Task '{removed_task['task']}' is deleted successfully!\n")
                break
            elif user_acceptance == False:
                print("Deleting is declined")
                break
            elif user_acceptance == None:
                continue
        break
def get_tasks (tasks):
    print("Your tasks: ")
    if not tasks:
        print("Your task list is empty")
    else:
        for j, task in enumerate(tasks, 1):
            status = "completed" if task['completed'] == True else "uncompleted"
            print(f"{j}. {task['task']} [{status}]")
def save_tasks(tasks, filename):
    print("Saving list ...")
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)
    print("List is saved.")
def toggle_task_completion(tasks):
    while True:
        get_tasks(tasks)
        print("\nPrint /close to exit")
        index_for_changing = input("Print task's index to change status : ")
        if check_for_close(index_for_changing):
            break
        index_for_changing = is_valid_index(index_for_changing, tasks)
        if index_for_changing == None:
            continue
        if tasks[index_for_changing]['completed']:
            tasks[index_for_changing]['completed'] = False
            print(f"Now '{tasks[index_for_changing]['task']}' is uncompleted")
            break
        else:
            tasks[index_for_changing]['completed'] = True
            print(f"Now '{tasks[index_for_changing]['task']}' is completed")
            break
def check_for_close(checkable_input):
    if checkable_input.strip().lower() == "/close":
        print("Exiting process...")
        return True
    return False
def is_valid_index(index, tasks):
    try:
        index = int(index)-1
    except ValueError:
        print("ERROR: Wrong value")
        return None
    if 0<=index<len(tasks):
        return index
    else:
        print("ERROR: Index is out of range")
        return None
def confirm_action (acceptance):
     if acceptance == "n":
         print("Stoping process ...")
         return False
     elif acceptance == "y":
         return True
     else:
         print("ERROR: Wrong input\n")
         return None
def main():
    filename = "myTasks.json"
    tasks=load_tasks(filename)
    print("Welcome to To-Do List!\n")
    while True:
        try:
            print("\n1. Show task list")
            print("2. Add task")
            print("3. Delete task")
            print("4. Change task's status")
            print("5. Close app\n")
            choice = input("Choose number of option : ").strip()
            if choice == '5':# Close procedure
                while True:
                    user_acceptance = confirm_action(input("\nExiting programm Y/N: ").strip().lower())
                    if user_acceptance:
                        save_tasks(tasks, filename)
                        print("Goodbye!")
                        break
                    elif user_acceptance == False:
                        break
                    elif user_acceptance == None:
                        continue
                if user_acceptance:
                    break
            elif choice == '1':#Get tasks
                get_tasks(tasks)
                input("Press enter to continue ...")  ################################################
            elif choice == '2': #Add task procedure
                add_task(tasks)
                input("Press enter to continue...")
            elif choice == '3':#Delete task procedure
                delete_task(tasks)
                input("Press enter to continue...")
            elif choice == '4':
                toggle_task_completion(tasks)
                input("Press enter to continue...")
            else:
                print("Wrong index number!")
        except ValueError:
            print("Wrong input value!\n")

if __name__ == "__main__":
    main()
