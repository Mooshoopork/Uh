# to find square root put sqrt
import math
print("To find the length of your line awnser the following questions.")
q = 0
while q == 0:
    w = 0
    while w == 0:
        x1 = int(input("Enter the x value of your first point: "))
        y1 = int(input("Enter the y value of your first point: "))
        print('Your first point is ({0},{1}).'.format(x1, y1))
        print("Is this correct?")
        b = 0
        while b == 0:
            print("yes = 1 no = 2")
            itc = int(input(""))
            if itc == 1:
                b = 1
                w = 1
            elif itc == 2:
                b = 1
                print("Ok, let's try again.")
            else:
                print("Input unclear, try again.")
    w = 0
    while w == 0:
        x2 = int(input("Enter the x value of your second point: "))
        y2 = int(input("Enter the y value of your second point: "))
        print('Your second point is ({0},{1}).'.format(x2, y2))
        print("Is this correct?")
        b = 0
        while b == 0:
            print("yes = 1 no = 2")
            itc = int(input(" "))
            if itc == 1:
                b = 1
                w = 1
            elif itc == 2:
                b = 1
                print("Ok, let's try again.")
            else:
                print("Input unclear, try again.")
    q = 1
d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
print()
print()
d = str(d)
print("The distance of the line is " + d + ".")
