# Modify the program to allow the user to input five numbers and find the largest number among them.
def find_largest_number():
    numbers = [float(input(f"Enter number {i+1}: ")) for i in range(5)]
    print(f"The largest number is: {max(numbers)}")

find_largest_number()
