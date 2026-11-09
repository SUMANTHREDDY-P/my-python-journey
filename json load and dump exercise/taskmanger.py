import json

def add_task():
    new_task=input("--- Add Contact ---\n")
    try :
        with open ("task.json", "r") as file:
            config = json.load(file)
    except Exception as e:
        config ={"task":[]}
    config["task"].append(f'{new_task}')
    with open("task.json", "w") as file:
        json.dump(config, file, indent=4)
    print(f"Task '{new_task}' added successfully!")


def all_tasks():

    with open ("task.json", "r") as file:
        config = json.load(file)
        tasks = config.get("task", [])
        if not tasks:
            print( "\n❌No tasks found! Your todo list is empty. 🎉")
        for i,task in enumerate(config["task"]):
            print(f'{i  + 1 }.{task} []')
        return


def delete_task():
    try:
        with open ("task.json", "r") as file:
            config = json.load(file)
        if not config.get("task"):
                print("No tasks available to delete.")
                return

        del_task = input("Enter task to delete: ")

        if del_task in config["task"] :
            config["task"].remove(del_task)
            print(f"Task '{del_task}' deleted successfully!")

            with open ("task.json", "w") as file:
                 json.dump(config, file, indent=4)
        else:
            print("Task not found.")

    except Exception as e:
        print(f"Task not found , {e}")

def run_task():
    while True:
        print("\n=== Task Manager ===")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Clear All Tasks")
        print("4. Exit")
        print()

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            tasks = all_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please pick 1, 2, 3, or 4.")



if __name__ == "__main__":
    run_task()

