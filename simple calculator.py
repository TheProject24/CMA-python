import math

mul = input("Do you want to perform mutiple values oprations? (y/n):")

if mul == "y":
    count = 0
    
    start = input("Do you want to start calculating? (y/n):")
    if start == "y":
        count += 1
    elif start == "n":
        print("Goodbye!")
    else:
        print("Invalid Syntax Error")
        
    while count > 0:
        a = int(input("Input the value of your first number: "))
        ops = input("The value of your operation symbol \n'+' for addition \n '-' for subtraction \n '*' for multiplication \n '/' for division : ")
        b = int(input("The value of your second number: "))
        
        if ops == '+':
            result = a + b
            print("You Chose addition")
        elif ops == '-':
            result = a - b
            print("You Chose subtraction")
        elif ops == '/':
            if b != 0:
                result = a / b
                print("You Chose division")
            else:
                print("Error in dividing by zero")
        elif ops == '*':
            result = a * b
            print("You Chose multiplication")
        else:
            print("Invalid Operator\n")
        
        print(f"Result of your operation {result}")
        
        choice = input("Do you want to perform another operation? (y/n):")
        if choice == 'y':
            count += 1
        elif choice == 'n':
            print("Good Bye")
            
if mul == "n":
    count = 0
    sin = input("Do you want to perform single values operations? (y/n):")
    
    if sin == "y":
        start = input("Do you want to start calculating? (y/n):")
        if start == "y":
            count += 1
        elif start == "n":
            print("Good Bye")
            count = 0
        while count > 0:
            a = int(input("input the value of your number"))
            ops = input("Input the operator sign \n'^' for square \n'2' for square-root \n'3' for cube \n 'sin' for sine \n'cos' for cosine \n:")
            
            if ops == "^":
                result = a*a
            elif ops == "2":
                result = math.sqrt(a)
            elif ops == "3":
                result = a*a*a
            elif ops == "sin":
                result = math.sin(a)
            elif ops == "cos":
                result = math.cos(a)
            else:
                print("Invalid operation")
            
            print(f"The result of the operation {result} \n")
            
            choice = input("Do you want to conduct another operation? (y/n):")
            if choice == "y":
                count += 1
            elif choice == "n":
                count = 0
                print("Good Bye")
    elif sin == "n":
        print("You're in the wrong program to meet your requirements")
    else:
        print("Invalid Input")