tasks = []
run_app = True
option = ""

#Prompts user for the task, then adds it to the task list, removing whitespaces on either end
def addTask():
    task = input("What task would you like to add?\n\n")
    task = task.strip()
    tasks.append(task)
    print(f"\n{task} successfully added!")


#Prmpts the user for what task they want to delete. Gives an error indicating capitals were messed up.
#Also gives an error if a task does not exist.
def deleteTask():
    task = input("What task would you like to delete?")
    task = task.strip()
    try:
        tasks.remove(task)
    except ValueError:
        capital = False
        task = task.lower()
        #Loop that checks if capitals were messed up by converting all tasks to lowercase
        for thisTask in tasks:
            if thisTask.lower() == task:
                print("Error: Check your capitalization!")
                capital = True
                break
        if capital == False:
            print("Error: Task does not exist!")

    else:
        print(f"{task} successfully removed!")
    finally:
        print("Execution complete!")

#Alerts the user if there are no tasks, otherwise, lists out the tasks
def viewTasks():
    if(len(tasks) == 0):
        print("Congratulations! You have no tasks!")

    else:
        print("\nTasks:")
        for task in tasks:
            print(f"•{task}")


print("\nWelcome to your fancy shmancy TODO List! The one stop shop for all your TODOing and tracking needs!")
while run_app:

    option = input("\nWhat would you like to do? \nView Tasks \nAdd Task \nDelete Task \nQuit\n\n")

    option = option.strip()

    option = option.lower()

    if option == "view tasks":
        viewTasks()

    elif option == "add task":
        addTask()

    elif option == "delete task":
        deleteTask()

    elif option == "quit":
        print("Closing TODO List...\nClosed!")
        run_app = False

    else:
        print("Error: Please select one of the four options:")


   

    