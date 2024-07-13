FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit) :
    
    temperature_in_cels = (fahrenheit-32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return temperature_in_cels

def convert_to_fahrenheit(celsius) :
    
    temperature_in_fahr = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return temperature_in_fahr

temperature = float(input("Enter the temperature to convert: "))
degree = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if degree == 'C':
    converted = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {converted}°F")
elif degree == 'F':
    converted = convert_to_celsius(temperature)
    print(f"{temperature}°F is {converted}°C")
else:
    print("Invalid degree. Please enter 'C' for Celsius or 'F' for Fahrenheit.")


    
