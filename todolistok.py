import json
import uuid
from datetime import datetime


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
            new_id = str(uuid.uuid4())
            current_date = datetime.now()
            tasks.append({'id': new_id,'task':task_input, 'status':"To Do", 'createdAt':current_date.strftime("%Y-%m-%d")})
            print(f"Task '{task_input}' is successfully added!\n")
            break
        else:
            print("Task can't be empty\n")
def update_task(tasks):
    while True:
        print("Update menu: ")
        get_all_tasks(tasks)
        print("Print /close to exit")
        task_index = input('Choose index of task to update : ')
        if check_for_close(task_index):
            break
        task_index = is_valid_index(task_index, tasks)
        if task_index == None:
            continue
        print(f'Changing: {tasks[task_index-1]['task']}')
        new_task = input("New task: ")
        if new_task.strip():
            tasks[task_index-1]['task'] = new_task
            print('Changes applyed\n')
            break
        else:
            print("Task cant be empty\n")
def delete_task (tasks):
    while True:
        print("Delete menu: ")
        get_all_tasks(tasks)
        print("Print /close to exit")
        index_for_delete = input("Write index of task to delete : ")
        if check_for_close(index_for_delete):
            break
        index_for_delete = is_valid_index(index_for_delete, tasks)
        if index_for_delete == None:
            continue
        while True:
            user_acceptance = confirm_action(input(f"Delete {index_for_delete}. {tasks[index_for_delete-1]['task']} ? Y/N : ").strip().lower())
            if user_acceptance:
                removed_task = tasks.pop(index_for_delete-1)
                print(f"Task '{removed_task['task']}' is deleted successfully!\n")
                break
            elif user_acceptance == False:
                print("Deleting is declined")
                break
            elif user_acceptance == None:
                continue
        break
def get_all_tasks (tasks):
    print("Your tasks: ")
    if not tasks:
        print("Your task list is empty\n")
        return None
    for j, task in enumerate(tasks, 1):
        print(f"{j}.  | id: {task['id']} | Task: '{task['task']}' | Status: '{task['status']}' | Created At: {task['createdAt']}")
def save_tasks(tasks, filename):
    print("Saving list ...")
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)
    print("List is saved.")
def toggle_task_completion(tasks):
    while True:
        get_all_tasks(tasks)
        print("\nPrint /close to exit")
        index_for_changing = input("Print task's index to change status : ")
        if check_for_close(index_for_changing):
            break
        index_for_changing = is_valid_index(index_for_changing, tasks)
        if index_for_changing == None:
            continue
        index_for_changing-=1
        while True:
            print(f"Changing '{tasks[index_for_changing]['task']}' status. \nChoose option : \n"
                  f"1 - To Do\n2 - In-Progress\n3 - Done")
            new_status = input('Your option : ')
            if check_for_close(new_status):
                break
            try:
                new_status = int(new_status)
            except ValueError:
                print("Wrong input type")
                continue
            if new_status == 1:
                tasks[index_for_changing]['status'] = "To Do"
                print(f"Task '{tasks[index_for_changing]['task']}' ")
                print(f"New status : {tasks[index_for_changing]['status']}")
            elif new_status == 2:
                tasks[index_for_changing]['status'] = "In-Progress"
                print(f"Task '{tasks[index_for_changing]['task']}' ")
                print(f"New status : {tasks[index_for_changing]['status']}")
            elif new_status == 3:
                tasks[index_for_changing]['status'] = "Done"
                print(f"Task '{tasks[index_for_changing]['task']}' ")
                print(f"New status : {tasks[index_for_changing]['status']}")
            else:
                print("ERROR: Wrong option index")
                continue
            break
        break
def check_for_close(checkable_input):
    if checkable_input.strip().lower() == "/close":
        print("Exiting process...")
        return True
    return False
def is_valid_index(index, tasks):
    try:
        index = int(index)
    except ValueError:
        print("ERROR: Wrong value")
        return None
    if 0<index<=len(tasks):
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
                get_all_tasks(tasks)
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
