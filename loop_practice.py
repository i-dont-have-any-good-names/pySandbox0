from os import system, name

def calculator(option, num1, num2):
    if option == "1":
        print(num1 + num2)
    elif option == "2":
        print(num1 - num2)
    elif option == "3":
        print(num1 * num2)
    elif option == "4":
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
                    print("1.Add")
                    print("2.Subtract")
                    print("3.Multiply")
                    print("4.Divide")
                    x = str(input("enter 1/2/3/4: "))
                    y = int(input("enter your first number: "))
                    z = int(input("enter your second number: "))
                    calculator(option=x, num1=y, num2=z)
                    continue
                else:
                    print("enter a valid option")
                    continue
        else:
            print("invalid password") 
            print("try again")
            continue
    else:
        print("invalid username")
print("Ended")