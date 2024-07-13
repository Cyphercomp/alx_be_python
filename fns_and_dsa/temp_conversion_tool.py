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

match degree :

    case "F"  :
        print(convert_to_celsius(temperature))
        print()

    case "C" :
        print(f"{temperature} is {convert_to_fahrenheit(temperature)}")
        print()

    case _ :
        print(" Invalid conversion degree !")

    
