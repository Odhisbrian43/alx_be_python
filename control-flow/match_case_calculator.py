#match-case operation

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
day = input("Enter the operation (+, -, *, /): ")

match day:
    case "+":
#operation == '+'
      num3 = num1 + num2
      print("The result is ", num3)
    case "-":
        num3 = num1 - num2
        print("The result is ", num3)
    case"*":
        num3 = num1 * num2
        print("The result is ", num3)
    case "/":
        num3 = num1 / num2
        if num2 > 0:
           print("The result is", num3)
        else:
           print("Cannot divide by zero.")
