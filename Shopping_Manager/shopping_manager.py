'''shopping_manager.py'''
'''This script manages the shopping list for a user. It allows adding, removing, changing and viewing items in the list.'''
'''The User can close the shopping list with a command.'''
'''The shopping list can be saved to a text file.'''
'''This script is only for exercise purposes.'''

# import necessary libraries and initialize variables
import sys
shopping_list = []

# Function definitions for managing the shopping list


def welcome():
    import time
    print("Welcome to your shopping list manager!")
    time.sleep(2)
    print()


def add_item(item):
    item = item.title()
    # add an item to the shopping list
    shopping_list.append(item)
    print(f"Added {item} to your shopping list.")


def change_item(old_item, new_item):
    # change an item in the shopping list
    old_item = old_item.strip().title()
    new_item = new_item.strip().title()
    if old_item in shopping_list:
        index = shopping_list.index(old_item)
        shopping_list[index] = new_item
        print(
            f"Changed {old_item} to {new_item} in your shopping list.")
    else:
        print(f"{old_item} not found in your shopping list.")


def delete_item(item):
    # delete an item from the shopping list
    item = item.strip().title()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"Deleted {item} from your shopping list.")
    else:
        print(f"{item} not found in your shopping list.")


def view_items():
    # view all items in the shopping list
    print("Your shopping list:")
    for item in shopping_list:
        print(f"- {item}")


def save_list():
    # safe list in txt file
    with open("shopping_list.txt", "w") as file:
        for item in shopping_list:
            file.write(f"{item}\n")


def close_list():
    # close the shopping list manager
    print("Closing the shopping list manager.")
    sys.exit()


# start the program


if __name__ == "__main__":
    welcome()
    while True:
        command = input(
            "Enter a command (add, change, delete, view, close or save): ").strip().lower()
        if command == "add":
            item = input("Enter the item to add: ").strip()
            add_item(item)
        elif command == "change":
            old_item = input("Enter the item to change: ").strip()
            new_item = input("Enter the new item: ").strip()
            change_item(old_item, new_item)
        elif command == "delete":
            item = input("Enter the item to delete: ").strip()
            delete_item(item)
        elif command == "view":
            view_items()
        elif command == "save":
            save_list()
            print("Shopping list saved to shopping_list.txt.")
        elif command == "close":
            close_list()
        else:
            print("Unknown command. Please try again.")
