#factorial program
a = 0
num = int(input("Input number here: "))
num1 = num - 1
num2 = num * num1
num -=1
while a == 0:
    num -=1
    if num != 0:
        num3 = num2 * num
        num2 = num3
    else:
        a = 1 
print(num2)

