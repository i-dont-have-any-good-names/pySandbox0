import time

num = int(input('enter count down number: ')) + 1
num0 = num
num1 = 1
speed = float(input("enter count down delay: "))

while num0 >= 0:
    num0 -= num1
    print(num0)
    time.sleep(speed)
    if num0 == 0:
        break
option = str(input("want to count up? y/n: "))
optionA = False
if option == "y":
    optionA = True
else:
    print("goodbye")
while optionA == True:
    while num0 < num - 1:
        num0 += num1
        print(num0)
        time.sleep(speed)
        if num0 <= num - 1:
            optionA = False