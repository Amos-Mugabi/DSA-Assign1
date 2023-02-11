# No. 8

# This function adds two numbers
def add(a, b):
    return a + b

# This function subtracts two numbers
def subtract(a, b):
    return a - b

# This function multiplies two numbers
def multiply(a, b):
    return a * b

# This function divides two numbers
def divide(a, b):
    return a / b


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")
    

    
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
       
        next_calculation = input("Do you want to continue? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")
