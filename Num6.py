# No.6.
def find_max(num1, num2, num3):
    
    maxnum = num1

    if num2 > maxnum:
        maxnum = num2

    if num3 > maxnum:
        maxnum = num3

    return maxnum

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

print("The maximum number is:", find_max(num1, num2, num3))
