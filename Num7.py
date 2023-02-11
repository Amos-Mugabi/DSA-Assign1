#No. 7

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

choice = input("Enter 'C' to convert from Celsius to Fahrenheit, or 'F' to convert from Fahrenheit to Celsius: ")
temperature = float(input("Enter the temperature: "))

if choice.upper() == 'C':
    result = celsius_to_fahrenheit(temperature)
    print("%.2f Celsius is equal to %.2f Fahrenheit" % (temperature, result))
elif choice.upper() == 'F':
    result = fahrenheit_to_celsius(temperature)
    print("%.2f Fahrenheit is equal to %.2f Celsius" % (temperature, result))
else:
    print("Invalid choice.")
