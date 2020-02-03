#Fibounaci Sequence
a = 0
num = 0
#0
print(num)
num =+ 1
# 1
print(num)
num2 = num + num
#1
print(num)
#2
print(num2)
while a == 0:
    if num < 13:
        num3 = num + num2
        #3
        print(num3)
        num = num2 + num3
        #5
        print(num)
        num2 = num + num3
        #8
        print(num2)
    else:
        a = 1
        