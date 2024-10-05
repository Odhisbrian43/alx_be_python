#Division calculator script.

def safe_divide(numerator, denominator):
    numerator = float(input)
    denominator = float(input)
    try:
        if denominator == 0:
           raise ZeroDivisionError ("Error: Cannot divide by zero.")
        else:
           return numerator / denominator
    except:
        str(numerator, denominator)
        raise ValueError ("Error: Please enter numeric values only.")

