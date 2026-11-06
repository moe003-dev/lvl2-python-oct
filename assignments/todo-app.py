database = []

while True:
    print("""
            1. Add to-do
            2. View to-do
            3. Edit to-do
            4. Delete to-do
            #  Exit
""")

    choice = input("Choice: ").strip()

    if choice == "1":
        todo = input("To-do: ").strip().capitalize()
        if todo == "":
            print("to-do cannot be empty")
        else:
            database.append(todo)
            print("To-do added")
    elif choice == "2":
        print("\nTo-do list")
        num = 1
        for items in database:
            print(f"{num}. {items}")
            num += 1
    elif choice == "3":
        edit_choice = int(input("Enter the number of the to-do you wish to edit: ").strip())
        new_todo = input("Enter the new to-do: ").strip().capitalize()
        database[edit_choice - 1] = new_todo
    elif choice == "4":
        delete_choice = int(input("Enter the number of the to-do to be deleted: ").strip())
        database.pop(delete_choice - 1)           
    elif choice == "#":
        print("Goodbye ...")
        break
    else:
        print("Please, Enter a valid option from those provided above")



# create a condition to check if user input for to-do is empty
