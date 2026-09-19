while True:
    answer = input("Do you want to add a new To-Do item? y/n: ")

    if answer == "y":
        todo = input("Enter your To-Do item: ")

        file = open("todo.txt", "a")
        file.write(todo + "\n")
        file.close()

    answer = input("Do you want to list your To-Do items? y/n: ")

    if answer == "y":
        file = open("todo.txt", "r")
        print(file.read())
        file.close()

    answer = input("Type exit to close or enter to continue: ")

    if answer == "exit":
        print("Thank you for using the To-Do program, come back again soon")
        break