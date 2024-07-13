
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
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print()
         
        elif choice == '2':
            # Prompt for and remove an item
            item_removed = input("enter the item to remove: ")
            shopping_list.remove(item_removed)
            print()
           
        elif choice == '3':
            # Display the shopping list
            print("The current shopping list")
            print("---------------------------")
            for item in shopping_list:
                print(item)
            print()
            
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()