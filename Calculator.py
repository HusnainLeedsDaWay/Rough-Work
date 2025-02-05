def calculator():
    while True:
        print("Welcome to the calculator!")
        print("Enter 'exit' to stop")

        num1 = input("Enter the first number: ")
        if num1.lower() == 'exit':
            break
        num1 = float(num1)

        operation = input("Enter operation (+, -, *, /): ")
        if operation.lower() == 'exit':
            break

        num2 = input("Enter the second number: ")
        if num2.lower() == 'exit':
            break
        num2 = float(num2)

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            result = num1 / num2
        else:
            print("Invalid operation")
            continue

        print("The result is: ", result)
        print("\n")

if __name__ == "__main__":
    calculator()
3