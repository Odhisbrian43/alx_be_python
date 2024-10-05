#Division calculator script.

def safe_divide(numerator, denominator):
    numbers = ["float(numerator)", "float(denominator)"]
    try:
        if denominator == 0:
           raise ZeroDivisionError ("Error: Cannot divide by zero.")
        else:
           return "float(numerator)" / "float(denominator)"
    except:
        numbers = ["str(numerator)", "str(denominator)"]
        raise ValueError ("Error: Please enter numeric values only.")

