def convert_temperature():
    print("\nWhich conversion do you want to choose:-")
    print("1. Celsius to Faranheit")
    print("2. Faranheit to Celsius")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        temp = float(input("Enter temperature in celsius: "))
        print(f"{temp} degree celsius is equal to {(temp*9/5)+32} degree faranheit.\n")
    elif choice == 2:
        temp = float(input("Enter temperature in faranheit: "))
        print(f"{temp} degree faranheit is equal to {(temp-32)*5/9} degree celsius.\n")
    else:
        print("Invalid input...please try again\n")
