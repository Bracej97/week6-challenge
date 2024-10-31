import json

def add():
    # Gather the users inputs for task and status
    task_input = input("Task: ")
    status_input = input("Status: ")

    # Write the task and status to a dictionary
    full_task = {
        "task": task_input,
        "status": status_input
    }

    with open("tasks.JSON", "r") as openfile:
        existing_tasks = json.load(openfile)

    existing_tasks.append(full_task)

    # Add dictionary to JSON file
    with open("tasks.JSON", "w") as outfile:
        json.dump(existing_tasks, outfile)

    print("Task has been added!")
    start()

def view():
    # Access the JSON file with the tasks in
    with open("tasks.JSON", "r") as openfile:
        to_do_list = json.load(openfile)
    num = 1

    # Iterate over the list and print the tasks from their dictionaries
    for task in to_do_list:
        print(f"{num}: {task['task']}   Status: {task['status']}")
        num += 1
    start()

def update():
        # Access the JSON file with the tasks in
    with open("tasks.JSON", "r") as openfile:
        to_do_list = json.load(openfile)
    num = 1

    # Iterate over the list and print the tasks from their dictionaries
    for task in to_do_list:
        print(f"{num}: {task['task']}   Status: {task['status']}")
        num += 1

    # Take the user input for which task they want to update, cathcing the error of not entering a number
    try:
        task_to_update_input = int(input("Which task do you want to update: "))
    except ValueError:
        print("Oops! You need to enter a number!")
        update()

    task_to_update = to_do_list[task_to_update_input - 1]

    updated_task = updating(task_to_update)



def updating(task):
    print("""
          Do you want to update:
          [ 1 ] Task
          [ 2 ] Status
          [ 3 ] Done
          """)

    try:
        part_to_update = int(input())
    except ValueError:
        print("Oops! You need to enter a number!")
        updating(task)

    if part_to_update == 1:
        updated_task = input(f"Old task: {task['task']}. New task: ")
        task["task"] = updated_task
    if part_to_update == 2:
        updated_status = input(f"Old status: {task['status']}. New status: ")
        task["status"] = updated_status
    if part_to_update == 3:
        return task

    updating()


def delete():
    # Access the JSON file with the tasks in
    with open("tasks.JSON", "r") as openfile:
        to_do_list = json.load(openfile)
    num = 1

    # Iterate over the list and print the tasks from their dictionaries
    for task in to_do_list:
        print(f"{num}: {task['task']}   Status: {task['status']}")
        num += 1

    # Take the user input for which task they want to delete, cathcing the error of not entering a number
    try:
        task_to_delete = int(input("Which task do you want to delete: "))
    except ValueError:
        print("Oops! You need to enter a number!")
        delete()

    to_do_list.pop(task_to_delete - 1)
    for task in to_do_list:
        num = 1
        print(f"{num}: {task['task']}   Status: {task['status']}")
        num += 1

    # Add dictionary to JSON file
    with open("tasks.JSON", "w") as outfile:
        json.dump(to_do_list, outfile)

    start()


def start():
    # Print the welcome statement to let the user know what they can do with the to-do list
    print(
        """
        Welcome to your to-do list. You can:

        [ 1 ] Add a task
        [ 2 ] View your tasks
        [ 3 ] Update a task
        [ 4 ] Delete a task
        [ 5 ] Exit
        """
    )

    # Allow the user to input their choice of what they want to do
    user_choice = input("Enter the number for what you want to do: ")

    # Run the command the user has chosen
    if user_choice == "1":
        add()
    if user_choice == "2":
        view()
    if user_choice == "3":
        update()
    if user_choice == "4":
        delete()
    if user_choice == "5":
        print("Thank you for viewing your to-do list.")
    else:
        print("You have made an invalid input. Please enter a number between 1 & 5")
        start()

start()
