def simple_calculator(num1, num2, operator):
    try:                         #dont need to add an isnumeric bc only numbers can be floats
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return "No.......enter numbers please, this is a calculator."

    
    if operator == "+":               #Logical operators
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            raise ValueError("Bro...you can't divide by zero!")
        result = num1 / num2
    else:
        raise ValueError("Operations should be in this form (+, -, *, /)")

    return result
