#Division calculator script.

def safe_divide(numerator, denominator):
    numbers = ["float(numerator)", "float(denominator)"]
    #float(numerator) = input()
    #float(denominator) = input()
    try:
        if denominator == 0:
           raise ZeroDivisionError ("Error: Cannot divide by zero.")
        else:
           return float(numerator) / float(denominator)
    except ValueError:
        print("Error: Please enter numeric values only.")
        #numbers = ["str(numerator)", "str(denominator)"]

