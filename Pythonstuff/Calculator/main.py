

def calculator(number1, operator, number2):
    try :
        return number1 operator number2
    except ValueError:
        print("You cannot divide by zero")


print(calculator(10,*,20))