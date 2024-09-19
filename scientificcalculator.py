import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def square_root(x):
    return math.sqrt(x)

def power(x, y):
    return math.pow(x, y)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def logarithm(x):
    if x <= 0:
        return "Error! Logarithm of non-positive number."
    return math.log(x)

def main():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Power")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")
    print("10. Logarithm")

    choice = input("Enter choice (1-10): ")

    if choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
        if choice in ['1', '2', '3', '4', '6']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

        if choice in ['1', '2', '3', '4', '6']:
            if choice == '1':
                print("Result: ", add(num1, num2))
            elif choice == '2':
                print("Result: ", subtract(num1, num2))
            elif choice == '3':
                print("Result: ", multiply(num1, num2))
            elif choice == '4':
                print("Result: ", divide(num1, num2))
            elif choice == '6':
                print("Result: ", power(num1, num2))
        elif choice in ['5', '7', '8', '9', '10']:
            num = float(input("Enter number: "))
            if choice == '5':
                print("Result: ", square_root(num))
            elif choice == '7':
                print("Result: ", sine(num))
            elif choice == '8':
                print("Result: ", cosine(num))
            elif choice == '9':
                print("Result: ", tangent(num))
            elif choice == '10':
                print("Result: ", logarithm(num))
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()
