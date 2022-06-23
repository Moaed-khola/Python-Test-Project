from lengths import *
from currency import *
from temperature import * 

print("===== Welcome to Value Converter =====")
print("===== New Commit =====")

while 1:
    print("Which option would you like to choose:-")
    print("1. Convert temperature")
    print("2. Convert currency")
    print("3. Convert lengths")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        convert_temperature()
    elif choice == 2:
        convert_currency()
    elif choice == 3:
        convert_lengths()
    elif choice == 4:
        print('Exiting...')
        exit(0)
