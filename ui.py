import db

# Display menu options, validation added
while True:
    choice = input("1. Add \n2. Remove \n3. View all \n4. Edit\n5. Quit\n")

    if choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5":
        print("Please try again, enter a number between 1 and 5..\n")

    # Ask user for juggler info to add
    elif choice == "1":
        name = input("Name?\n")
        country = input("Country?\n")
        catches = input("Catches?\n")
        db.add_juggler(name, country, catches)

    # Ask user for juggler info to remove
    elif choice == "2":
        name = input("Name?\n")
        db.remove_juggler(name)

    # Show all jugglers in db
    elif choice == "3":
        db.show_all()

    # Ask user to update high score for juggler named
    elif choice == "4":
        name = input("Name?\n")
        catches = input("New high score?\n")
        db.edit(name, catches)

    # Exit
    elif choice == "5":
        break