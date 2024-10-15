import json
from collections import deque

def load_tasks(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"{filename} is not found. New file will be created when you add your first task")
        return []
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
            print("Task can't be empty\n")
def update_task(tasks):
    while True:
        print("Update menu: ")
        get_tasks(tasks)
        print("Print /close to exit")
        task_index = input('Choose number of task to update : ')
        if check_for_close(task_index):
            break
        task_index = is_valid_index(task_index, tasks)
        if task_index == None:
            continue
        print(f'Changing: {tasks[task_index]['task']}')
        new_task = input("New task: ")
        if new_task.strip():
            tasks[task_index]['task'] = new_task
            print('Changes applyed\n')
            break
        else:
            print("Task cant be empty\n")
def delete_task (tasks):
    while True:
        print("Delete menu: ")
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
        print("Your task list is empty\n")
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
            if tasks:
                print("3. Update task")
                print("4. Delete task")
                print("5. Change task's status")
            print("6. Exit and save changes\n")
            choice = input("Choose number of option : ").strip()
            if choice == '6':# Close procedure
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
            elif choice == '3' and tasks:  # Update task procedure
                update_task(tasks)
                input("Press enter to continue...")
            elif choice == '4' and tasks:#Delete task procedure
                delete_task(tasks)
                input("Press enter to continue...")
            elif choice == '5' and tasks:
                toggle_task_completion(tasks)
                input("Press enter to continue...")
            else:
                print("Wrong index number!")
        except ValueError:
            print("Wrong input value!\n")

if __name__ == "__main__":
    main()
