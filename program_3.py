# Program 3
# Write a menu-driven program to perform arithmetic operations.

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def modulo(x, y):
    return x % y


def floor(x, y):
    return x // y


print("""
        ----------------------
       | ARITHMETIC OPERATORS |
        ----------------------
       | 1. Add        +      |
       | 2. Subtract   -      |
       | 3. Multiply   *      |
       | 4. Divide     /      |
       | 5. Modules    %      |
       | 6. Floor Division // |
        ----------------------
""")
while True:

    choice = input("Enter choice(1/2/3/4/5/6): ")

    if choice in ('1', '2', '3', '4', '5', '6'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        elif choice == '5':
            print(num1, "%", num2, "=", modulo(num1, num2))
        elif choice == '6':
            print(num1, "//", num2, "=", floor(num1, num2))
    else:
        print("Invalid Input")
        break
