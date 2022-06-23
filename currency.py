def convert_currency():
    print("\nWhich conversion do you want to choose:-")
    print("1. Dollar to pound")
    print("2. Pound to Dollar")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        value = float(input("Enter currency in dollars: "))
        print(f"{value} dollars in pounds will be {value*0.73}\n")
    elif choice == 2:
        value = float(input("Enter currency in pounds: "))
        print(f"{value} pounds in dollars will be {value/0.73}\n")
