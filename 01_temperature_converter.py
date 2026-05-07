def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit}°F is equivalent to {celsius:.2f}°C")

def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    print(f"{celsius}°C is equivalent to {fahrenheit:.2f}°F")
    
choice = input("C/F: ")
temp = float(input("temperature: "))

if choice == "F":
    fahrenheit_to_celsius(temp)
else:
    celsius_to_fahrenheit(temp)