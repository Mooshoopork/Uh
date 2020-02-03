try:
    num1=input("Input your first number: ")
    num2=input("Input your second number: ")
    num3=input("Input your last number: ")
except:
    print("Please only enter numbers.")

list = ([num1, num2, num3])
list.sort()
print()
print("The median is:", list[1])