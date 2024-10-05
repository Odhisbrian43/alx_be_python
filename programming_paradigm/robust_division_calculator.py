#Division calculator script.

def safe_divide(numerator, denominator):
    numbers = ["float(numerator)", "float(denominator)"]
    #float(numerator) = input()
    #float(denominator) = input()
    try:
        if float(denominator) == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")
        else:
            #return f"The result of the division is " 
            result = float(numerator) / float(denominator)
            return f"The result of the division is {result}"
    except ValueError:
        return "Error: Please enter numeric values only."
        #numbers = ["str(numerator)", "str(denominator)"]

