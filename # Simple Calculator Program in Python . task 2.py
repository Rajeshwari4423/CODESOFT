def add(a, b):
    return a + b

def subtract(a , b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    else:
        return a / b

def main():
    print("Select Operators:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        try:
            choice = input("Enter choice(1/2/3/4): ")

            if choice == 'q':
                print("Exiting the calculator.")
                break

            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            else:
                print("Invalid input, please choose from 1, 2, 3, or 4.")
            
            next_calculation = input("Do you want another calculation? (yes/no): ")
            if next_calculation.lower() != 'yes':
                print("Exiting the calculator.")
                break
        
        except ValueError:
            print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()
