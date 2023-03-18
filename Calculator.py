#Calculator

print("Hello and welcome to Rapid Calculator")
operation = input("What operation would you like to carry out? '+', '-' '*' '/': ")
if operation == "+":
    num1 = input("What is your first digit? ")
    num2 = input("What is your second digit? ")
    sum = float(num1) + float(num2)
    print("The sum is: " + str(sum))
elif operation == "-":
    num1 = input("What is your first digit? ")
    num2 = input("What is your second digit? ")
    diff = float(num1) - float(num2)
    print("The difference is: " + str(diff))
elif operation == "*":
    num1 = input("What is your first digit? ")
    num2 = input("What is your second digit? ")
    prod = float(num1) * float(num2)
    print("The product is: " + str(prod))
elif operation == "/":
    num1 = input("What is your first digit? ")
    num2 = input("What is your second digit? ")
    div = float(num1) / float(num2)
    print("The result is: " + str(div))
else:
    print("Error! This operation is invalid")
