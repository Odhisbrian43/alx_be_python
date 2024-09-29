#function for arithmetics

def perform_operation(num1, num2, operation):

    match operation:

        case "add":

            num1 + num2 = result

            print("Result: ", result)

        case "subtract":

            num1 - num2 = result

            print("Result: ", result)

        case "multiply":

            num1 * num2 = result

            print("Result: " result)

        case "divide":
            
            if num2 > 0:

                num1 / num2 = result

                print("Result: ", result)

            else:

                print("Cannot divide by zero")
        case _:

            print("Invalid operation entered, try again.")

perform_operation()



