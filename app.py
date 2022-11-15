import math

qfa = str(input("Type one of the following: cal, n\n"))


if qfa == "n":
    print("Ended")
elif qfa == "cal":
    math = str(input("Enter one of the following: ma, ms, mm, md, mdr, me\n"))
    if math == "ma":
        print('mode: "ma"')
        num1 = int(input("Enter your first number.\n"))
        num2 = int(input("Enter your second number.\n"))
        sum = num1 + num2
        print("The sum of this problem is\n" + str(sum))
    elif math == "ms":
        print('mode: "ms"')
        num1 = int(input("Enter your first number.\n"))
        num2 = int(input("Enter your second number.\n"))
        sum = num1 - num2
        print("The difference of this problem is\n" + str(sum))
    elif math == "mm":
        print('mode: "mm"')
        num1 = int(input("Enter your first number.\n"))
        num2 = int(input("Enter your second number.\n"))
        sum = num1 * num2
        print("The sum of this problem is\n" + str(sum))
    elif math == "me":
        print('mode: "me"')
        num1 = int(input("Enter your first number.\n"))
        num2 = int(input("Enter your second number.\n"))
        sum = num1 ** num2
        print("The sum of this problem is\n" + str(sum))
    elif math == "md":
        print('mode: "math division"')
        num1 = int(input("Enter your first number.\n"))
        num2 = int(input("Enter your second number.\n"))
        sum = num1 / num2
        print("The sum of this problem is\n" + str(sum))
    elif math == "mdr":
        print('mode: "math division with remainders"')
        num1 = int(input("Enter your first number.\n"))
        num2 = int(input("Enter your second number.\n"))
        sum = num1 % num2
        print("The remainder of this devision problem is\n" + str(sum))
    else:
        print("Enter something valid")