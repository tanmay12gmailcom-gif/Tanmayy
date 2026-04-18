try:
    num1 = int(input("enter first value: "))
    num2 = int(input("enter second value: "))
    division = num1 / num2
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("number cannot divide by zero")
    print("Cannot divide by zero!")
except ValueError:
    print("invalid input")
else:
    print("ans:", division)
    print("Please enter numbers only!")