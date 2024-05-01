#Inicialize
todo = []
print("Welcome To Py-Todo APP!!\nMade by Bagi763")

#Define Functions
def add(Task):
    todo.append(Task)
    print(f"\nThe Task '{Task}' was Added to The ToDo List!")

def edit(Task, Edit):
    if Task in todo:
        todo.insert(todo.index(Task), Edit)
        todo.remove(Task)
        print(f"The Task: '{Task}' is Now '{Edit}'!!")
    else:
        print(f"Error: The Task: '{Task}' is not on The List")

def delete(Task):
    todo.remove(Task)
    print(f"The Task: {Task} has been Deleted!!")

#Run Program
while True:
    print("\nWhat Command You Want to Run?")
    print("-------------------------------")
    print("List: Show The ToDo List")
    print("Add: Add a Task to The ToDo List")
    print("Edit: Edit a Task on The ToDo List")
    print("Delete: Delete a Task on The ToDo List")
    print("Quit: Quit The APP")
    print("More: More of Bagi763")
    command = input("Command: ")
    if command == "List" or command == "list":
        if len(todo) != 0:
            print(f"\n{todo}")
        else:
            print("\nList Is Empty")
    elif command == "Add" or command == "add":
        add(input("Task: "))
    elif command == "Edit" or command == "edit":
        print(f"\nWhat Task You Want to Edit (Insert Task Number on The List)?\n{todo}")
        edit(input("Task: "), input("Edit: "))
    elif command == "Delete" or command == "delete":
        print(f"\nWhat Task You Want to Delete?\n{todo}")
        delete(input("Task: "))
    elif command == "Quit" or command == "quit":
        break
    elif command == "More" or command == 'more':
        print("\n\n\n------------------------------------------")
        print("Github Profile: https://github.com/Bagi763\nBe-Team: https://github.com/be-rep")
        print("------------------------------------------\n\n\n")
    else:
        print("\nError: Invalid Command")
print("\n\nBye!!")
