def operation_main(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero"
    elif operation == "subtract":
        return num1 - num2
    else:
        return "Invalid operator"


num1 = int(input("Enter the first number => "))
num2 = int(input("Enter the second number => "))
operation = input("enter opration(add,multiply,divide,subtract) =>")


result = operation_main(num1, num2, operation)
print("Result:", result)
