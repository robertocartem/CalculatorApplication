''' Building a sophisticated calculator 
that can handle addition, subtraction,
multiplication, and division operations'''

print("++--++--++-- Welcome to My Calculator --++--++--++")

# Set up a loop that continuously takes user input 
while True:
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")

    choice = input("Enter a choice (1/2/3/4/5): ")

    if choice == "5":
        print("Thank you for using My Calculator. Have a great day!")
        break

# Handling invalid choices
    if choice not in ("1", "2", "3", "4", "5"):
        print("Invalid choice. Please enter a valid option")
        continue # Restart the loop

# Inside the loop, implement each operation based on the user's choice
    elif choice in ("1", "2", "3", "4"):
        num1 = float(input("Enter the first number:"))
        num2 = float(input("Enter the second number:"))

        if choice == "1":
                result = num1 + num2
                print("Result:", result)

        elif choice == "2":
                result = num1 - num2
                print("Result:", result)

        elif choice == "3":
                result = num1 * num2
                print("Result:", result)

        elif choice == "4":
                if num2 != 0:
                    result = num1 / num2
                    print("Result:", result)
                else:
                    print("Cannot divide by zero")

        
    