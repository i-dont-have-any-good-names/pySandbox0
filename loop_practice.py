def calculator(option, num1, num2):
    if option == "a":
        print(num1 + num2)
    elif option == "s":
        print(num1 - num2)
    elif option == "m":
        print(num1 * num2)
    elif option == "d":
        print(num1 / num2)

running = True
while running:
    name = input("enter your username: ")
    login = False
    if name == "cart21":
        print(name)
        password = input("enter your password: ")
        passL = False
        if password == "qwe":
            print("login seccessful")
            login = True
            while login:
                options = input("want to use a calculator(c) or end(n)?: ")
                if options == "n":
                    login = False
                    running = False
                elif options == "c":
                    x = str(input("enter a or s or m or d"))
                    y = int(input("enter your first number: "))
                    z = int(input("enter your second number: "))
                    calculator(option=x, num1=y, num2=z)
                    continue
        
        else:
            print("invalid password")
            continue
    else:
        print("invalid username")

