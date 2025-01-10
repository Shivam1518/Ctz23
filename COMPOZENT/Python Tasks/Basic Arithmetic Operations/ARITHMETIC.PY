def basic_arithmetic_operations():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    print(f"Addition: {num1 + num2}")
    print(f"Subtraction: {num1 - num2}")
    print(f"Multiplication: {num1 * num2}")
    print(f"Division: {num1 / num2 if num2 != 0 else 'Cannot divide by zero'}")

basic_arithmetic_operations()