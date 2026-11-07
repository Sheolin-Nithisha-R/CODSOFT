# CODSOFT Python Programming Internship
# Task 2: Simple Calculator
# Developed by: Sheolin Nithisha R

def calculator():
    print("--- SIMPLE CALCULATOR ---")
    print("Operations: +  -  *  /  %")
    
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operation (+, -, *, /, %): ")
        num2 = float(input("Enter second number: "))
        
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error! Division by zero is not allowed.")
                return
        elif op == '%':
            result = num1 % num2
        else:
            print("Invalid operation!")
            return
            
        print(f"\nResult: {num1} {op} {num2} = {result}")
        
    except ValueError:
        print("Please enter valid numbers!")

# Main
while True:
    calculator()
    choice = input("\nDo you want to calculate again? (yes/no): ").lower()
    if choice != 'yes' and choice != 'y':
        print("Thank you for using Calculator! - CODSOFT")
        break