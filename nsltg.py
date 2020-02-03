num1 = input("Type your first number: ")
num2 = input("Type your second number: ")
num3 = input("Type your third number: ")

n1 = float(num1)
n2 = float(num2)
n3 = float(num3)

if n1 != n2 and n2 != n3 and n3 != n1:
    if n1 > n2 and n1 > n3:
        n = n1
    if n2 > n1 and n2 > n3:
        n = n2
    if n3 > n1 and n3 > n2:
        n = n3
    print(" ")
    print("The biggest number is: ", n)
elif n1 > n2 or n1 > n3:
    print("The biggest number is: ",n1)
elif n2 > n1 or n2 > n3:
    print("The biggest number is: ", n2)
elif n3 > n1 or n3 > n2:
    print("The biggest number is: ", n3)
else:
    print("There is a problem! All of the numbers are equal")
    

