
def display_menu():
    print("---------------------------")
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        print("---------------------------")
        print()

        if choice == '1':
            item = input("add an item to the shopping list: ")
            shopping_list.append(item)
            print()
            pass
        elif choice == '2':
            # Prompt for and remove an item
            item_removed = input("enter item to be removed from the shopping list: ")
            shopping_list.remove(item_removed)
            print()
            pass
        elif choice == '3':
            # Display the shopping list
            print("The current shopping list")
            print("---------------------------")
            for item in shopping_list:
                print(item)
            print()
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()