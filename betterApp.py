def cal():
    print("start or none to end")
    option = str(input())
    
    if option == "none":
        print("Ended")
    elif option == "start":
        print("Calculator started.")
        num1 = int(input("enter your first number\n"))
        equation = str(input("enter your operation\n"))
        num2 = int(input("enter your second number\n"))
        if equation == "+":
            print('"addition"\n')
            sum = num1 + num2
            print(sum)
        elif equation == "-":
            print('"subtraction"\n')
            sum = num1 - num2
            print(sum)
        elif equation == "*":
            print('"mutiplication"\n')
            sum = num1 * num2
            print(sum)
        elif equation == "/":
            print('"division"\n')
            sum = num1 / num2
            print(sum)
        elif equation == "^":
            print('"exponent"\n')
            sum = num1 ** num2
            print(sum)
        else:
            print("enter a vaid value")
    else:
        print("enter a valid value")
        
optionB = str(input("open cal or none\n"))

if optionB == "cal":
    cal()
elif optionB == "none":
    print("ended")
else:
    print("enter something valid")