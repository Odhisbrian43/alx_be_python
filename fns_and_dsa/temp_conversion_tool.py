#Temperature conversion

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

temp = int(input("Enter the temperature to convert: "))

unit = input("Is this temperature in Celsius or Fahrenheit? (C/F):" )

if unit == "F":

    def convert_to_celsius(fahrenheit):

        result = (temp - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

        print(f"{temp}°F is {result}°C")

    convert_to_celsius()

elif unit == "C":

    def convert_to_fahrenheit(celsius):

       result1 = (temp + 32) * CELSIUS_TO_FAHRENHEIT_FACTOR

       print(f"{temp}°C is {result1}°F")

    convert_to_fahrenheit()

else:

    print("invalid input, try again.")


