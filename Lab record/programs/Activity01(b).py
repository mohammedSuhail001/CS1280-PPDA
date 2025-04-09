# Modify the temperature converter program to include conversions between Celsius, Fahrenheit, and Kelvin. 
def convert_temperature():
    while True:
        units = {'1': 'C', '2': 'F', '3': 'K'}
        print("\nConvert from: 1. Celsius  2. Fahrenheit  3. Kelvin  4. Quit")
        choice = input("Enter choice (1-3) or '4' to quit: ")
        
        if choice == '4':
            break
        if choice not in units:
            print("Invalid input. Try again.")
            continue
        
        temp = float(input(f"Enter temperature in {units[choice]}: "))
        c = temp if choice == '1' else (temp - 32) * 5/9 if choice == '2' else temp - 273.15
        f, k = (c * 9/5) + 32, c + 273.15
        print(f"{temp}{units[choice]} = {c:.2f}C = {f:.2f}F = {k:.2f}K")

convert_temperature()
