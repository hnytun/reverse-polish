import sys
import math

#function that takes an operation and a stack, and operates on the stack
#with the respective operation
def operateStack(operation, stack):
    if operation == "+":
        stack.append(stack.pop()+stack.pop())
    elif operation == "*":
        stack.append(stack.pop()*stack.pop())
    elif operation == "/":
        #special case, since we need to divide left to right
        right = stack.pop()
        left = stack.pop()
        stack.append(left/right)
    elif operation == "v":
        stack.append(math.sqrt(stack.pop()))
    elif operation == "sin":
        stack.append(math.sin(stack.pop()))
    elif operation == "cos":
        stack.append(math.cos(stack.pop()))
    elif operation == "p":
        print(stack[-1])

#create empty list
stack = list()

#check if argument is set which means that the user has a reverse polish notation ready
#(hopefully)
if len(sys.argv) > 1:
    #userinput
    userInputList=sys.argv[1].split(" ")

    #iterate over every space-separated symbol
    for i in userInputList:
        try: #if its a number, we add it to the stack
            number=float(i)
            stack.append(number)
        except ValueError: # if its a operator, we operate the stack
            operateStack(i,stack)
    print("sum of: ")
    print(sys.argv[1])
    print("=")
    print(stack)

#if argument is not set, we calculate interactively
else:
    while True:
        #take input from user(may be more than one operation)
        operation=(input("input: "))
        userInputList = operation.split(" ")

        for i in userInputList:
        #if its a number, we add to stack, if not(int error), we operate on
        #stack
            try:
                number=float(i)
                stack.append(number)
            except ValueError:
                operateStack(i,stack)

        #print stack for reference, can be commented out, but i prefer
        #having a visual of the stack since its a interactive rpn calculator
        #print(stack)
