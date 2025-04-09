def temperature_converter():
	print("Temperature converter")
	temp = float(input("Enter temperature:"))
	print("Convert to:")
	print("1.Celcius to Fahrenheit")
	print("2.Fahrenheit to Celcius")
	choice = input("ENter choice(1/2):")
	if choice == '1':
		fahrenheit = (temp * 9/5) + 32
		print(F"{temp}^C is {fahrenheit}^F")
	elif choice == '2':
		celcius = (temp - 32) * 5/9
		print(f"{temp}^F is {celcius}^C")
	else:
		print("Invalid Input")
temperature_converter()
