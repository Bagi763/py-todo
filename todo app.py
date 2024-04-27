#Set The ToDo List to The Originial File
todo = []
with open("py todo app\main\list.txt", "r") as rf:
    for line in rf:
        todo.append(line)
print(todo)

#Ask For a Command
while True:
    command = input("What Command You Want to Run?\nAvailable Commands: add\nCommand:")

    #Check The Command Given
    if command == "add":
        todo.append(input("What Chore You Want to Add?\nChore:"))
        length = len(todo)
        print("ToDo List:")
        for i, item in enumerate(todo):
            if i != length - 1:
                print(item, end=" ,")
    else:
            print(item, end=" ")
    print(todo)

    #Add The Chore to The File
    with open("py todo app\main\list.txt", "w") as wf:
        wf.write("")
    with open('py todo app\main\list.txt', "a") as af:
        for item in todo:
            af.write(item + "\n")

#ToDo List (lol):
#1) Finish The First Segment
#2) Add View
#3) Add Edit
#4) Make It A Little More Fancy
#5) Add Description (why not?)