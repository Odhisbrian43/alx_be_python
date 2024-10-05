#Division calculator script.

def safe_divide(numerator, denominator):
    numbers = ["float(numerator)", "float(denominator)"]
    #float(numerator) = input()
    #float(denominator) = input()
    try:
        result = float(numerator) / float(denominator)
        return f"The result of the division is {result}"
        #if float(denominator) == 0:
            #raise 
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        #else:
            #return f"The result of the division is " 
    except ValueError:
        return "Error: Please enter numeric values only."
        #numbers = ["str(numerator)", "str(denominator)"]

