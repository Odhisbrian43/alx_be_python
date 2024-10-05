#Division calculator script.

def safe_divide(numerator, denominator):
    numbers = ["float(numerator)", "float(denominator)"]
    #float(numerator) = input()
    #float(denominator) = input()
    try:
        if denominator == 0:
            raise ZeroDivisionError:
                print("Error: Cannot divide by zero.")
        else:
           result = float(numerator) / float(denominator)
           return f"The result of the division is {result}"
    except ValueError:
        print("Error: Please enter numeric values only.")
        #numbers = ["str(numerator)", "str(denominator)"]

