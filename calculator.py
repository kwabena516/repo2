print("\t\tWELCOME TO THE PYTHON CALCULATOR!")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operation = int(input("\nSelect an operation to perform: "
                      "\n1. Addition (+) "
                      "\n2. Subtraction (-) "
                      "\n3. Multiplication (*) "
                      "\n4. Division (/)\n"))


def addition (num1, num2):
    sum = num1 + num2
    return sum


def subtraction(num1, num2):
    difference = num1 - num2
    return difference


def multiplication (num1, num2):
    product = num1 * num2
    return product


def division (num1, num2):
    quotient = round(num1 / num2),2
    return quotient


if operation == 1:
    print("\nThe sum of the numbers is: " + str(addition(num1,num2)))
elif operation == 2:
    print("\nThe difference between the numbers is: " + str(subtraction(num1,num2)))
elif operation == 3:
    print("\nThe product of the two numbers is: " + str(multiplication(num1,num2)))
elif operation == 4:
    print("\nThe quotient of the numbers is: " + str(division(num1,num2)))

choice = input("Would you like to use the calculator again? (y/n)")
if choice == "y"

