# to_do_list.py
# Author: hajar1010
# Description: A command-line to-do list app to add, view, and complete tasks.

task_list=[]
done=False
while True:
    
    user_choice=input("** Menu: **\n-------------\n- add a task\n- show all tasks\n- mark a task as done\n- delete a task\n- save tasks to a file\n- exit\n-------------\nEnter a valid action : ").strip().lower()

    if user_choice=="add a task":
        new_task=input("type your new task : ").strip()
        task_list.append([new_task,done])
        print(f'Task "{new_task}" added.')

    elif user_choice=="show all tasks":
        if not task_list:
            print("No tasks found.")
        else:
            print("Your tasks:")
            j=1
            for i in task_list:
                print(j,")" ,i)
                j+=1

    elif user_choice=="mark a task as done":
        if not task_list:
            print("No tasks to mark done.")
            continue
        else:
            number =int(input("What is the number of the task : "))
            if 1 <= number <= len(task_list):
                task_list[number - 1][1] = True
                print(f'Task "{task_list[number - 1][0]}" marked as done.')
            else:
                print("Invalid task number.")

    elif user_choice=="delete a task":
        if not task_list:
            print("No tasks to delete.")
            continue
        else:
            number1 = int(input("What is the number of the task : "))
            task_list.pop(number1-1)
            print("a task was deleted")

    elif user_choice=="save tasks to a file":
        with open("to-do-list.txt", "w") as file:
            for task, done in task_list:
                file.write(f"{task}::{done}\n")
        print("Tasks saved to 'to-do-list.txt'.")

    elif user_choice == "exit":
        print("Goodbye!")
        break
    else:

        print("Invalid choice  enter a valid action from the menu")
