def convert_lengths():
    print("\nWhich conversion do you want to choose:-")
    print("1. Centimeters to foot and inches")
    print("2. Foot and inches to centimeter")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        value = float(input("Enter length in cm: "))
        inches = value/2.54
        feet = inches/12
        print(f"{value} centimeters in equal to {feet} feet and {inches} inch\n")
    elif choice == 2:
        feet = float(input("Enter length in feet: "))
        inches = float(input("Enter length in inches: "))
        length = (feet*12 + inches)*2.54
        print(f"{feet} feet and {inches} inches in centimeters will be {length}\n")
