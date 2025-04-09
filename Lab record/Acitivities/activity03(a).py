# Write a program that performs additional operations on the list such as sorting and reversing the list, in addition to insert, delete, and find operations.
def list_operations():
    lst = [1, 2, 3, 4, 5]
    while True:
        print("\nChoose an operation:")
        print("1. Insert element")
        print("2. Delete element")
        print("3. Find element")
        print("4. Sort list")
        print("5. Reverse list")
        print("6. Exit")
        
        print(f"Current list: {lst}")
        choice = input("Enter choice (1-6): ")
        
        if choice == '1':
            try:
                element = int(input("Enter integer element to insert: "))
                lst.append(element)
                print(f"Inserted {element}. Updated list: {lst}")
            except ValueError:
                print("Invalid input! Please enter an integer.")
        elif choice == '2':
            try:
                element = int(input("Enter integer element to delete: "))
                if element in lst:
                    lst.remove(element)
                    print(f"Deleted {element}. Updated list: {lst}")
                else:
                    print("Element not found.")
            except ValueError:
                print("Invalid input! Please enter an integer.")
        elif choice == '3':
            try:
                element = int(input("Enter integer element to find: "))
                print("Element found" if element in lst else "Element not found")
            except ValueError:
                print("Invalid input! Please enter an integer.")
        elif choice == '4':
            lst.sort()
            print(f"List sorted: {lst}")
        elif choice == '5':
            lst.reverse()
            print(f"List reversed: {lst}")
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

list_operations()
