#3rd question
#prompt: get the input of 2 numbers and show the option to choose an operation to make like + * / math 

number1 = int(input("Type the 1st number: "))
number2 = int(input("Type the 2nd number: "))

operation = input("Type the operation (+, *, /, pow): ")

result = None

if operation == "+":
    result = number1 + number2
elif operation == "*":
    result = number1 * number2
elif operation == "/":
    result = number1 / number2
elif operation == "pow":
    result = pow(number1, number2)
else:
    print("Invalid operation.")

if result is not None:
    print("Result:", result)