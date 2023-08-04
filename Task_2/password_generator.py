#                                     Task 2

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y                              


print("Select operation.")
print("A). Add\nB). Subtract\n3). Multiply\n4). Divide")

while True: # while loop is True than excute
    # take input from the user
    choice = input("Enter choice: A, B, C, D \nAnswer: ")

    # check if choice is one of the four options
    if choice in ('A', 'B', 'C', 'D'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 'A':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == 'B':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == 'C':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == 'D':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
                    # break the while loop if answer is no
            break
    else:
        print("Invalid Input")