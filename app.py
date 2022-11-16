qfa = str(input("Type one of the following: dob cal, cal, n\n"))


if qfa == "n":
    print("Ended")
elif qfa == "cal":
    math = str(input("Enter one of the following: ma, ms, mm, md, mdr, me\n"))
    if math == "ma":
        print('mode: "ma"')
        num1 = int(input("Enter your first number.\n"))
        num2 = int(input("Enter your second number.\n"))
        numSum = num1 + num2
        print("The sum of this problem is\n" + str(sum))
    elif math == "ms":
        print('mode: "ms"')
        num1 = int(input("Enter your first number.\n"))
        num2 = int(input("Enter your second number.\n"))
        numSum = num1 - num2
        print("The difference of this problem is\n" + str(sum))
    elif math == "mm":
        print('mode: "mm"')
        num1 = int(input("Enter your first number.\n"))
        num2 = int(input("Enter your second number.\n"))
        numSum = num1 * num2
        print("The sum of this problem is\n" + str(sum))
    elif math == "me":
        print('mode: "me"')
        num1 = int(input("Enter your first number.\n"))
        num2 = int(input("Enter your second number.\n"))
        numSum = num1 ** num2
        print("The sum of this problem is\n" + str(sum))
    elif math == "md":
        print('mode: "math division"')
        num1 = int(input("Enter your first number.\n"))
        num2 = int(input("Enter your second number.\n"))
        numSum = num1 / num2
        print("The sum of this problem is\n" + str(sum))
    elif math == "mdr":
        print('mode: "math division with remainders"')
        num1 = int(input("Enter your first number.\n"))
        num2 = int(input("Enter your second number.\n"))
        numSum = num1 % num2
        print("The remainder of this devision problem is\n" + str(sum))
    else:
        print("Enter something valid")

elif qfa == "dob cal":
    age = int(input())
    dob = 2022 - age
    agea = dob - 1
    if age >= 2022:
        print("Error enter a number less than 2022")
    elif age < 2022:
        print("The year you were born was\n" + str(dob) + "-" + str(dob - 1))
    else:
        print("Enter a number")
else:
    print("Enter something valid")