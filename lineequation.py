print("To find the slope intersect form of your line, please awnser the following questions.")
print("")
print("First we need a slope. Do you already know your slope?")
b = 0
while b == 0:
    print("yes = 1 no = 2")
    itc = int(input(""))
    if itc == 1 or itc == 2:
        b = 1
    else:
        print("Input unclear, try again.")
if itc == 1:
    m = int(input("What is your slope? "))
    q = 1
    print("Do you have at least one point?")
    b = 0
    while b == 0:
        print("yes = 1 no = 2")
        itc = int(input(""))
        if itc == 1:
            b = 1
            point = 1
        elif itc == 2:
            b = 1
            k = 0
            print("Do you have a y-intersept?")
            # Edit here
    while k == 0:
        print("yes = 1 no = 2")
        f = int(input(""))
        if f == 1:
            k = 1
        elif f == 2:
            k = 1
        else:
            print("Input unclear, try again.")
elif itc != 1 or itc != 2:
    print("Input unclear, try again.")
    while point == 1:
            w = 0
            while w == 0:
                x = int(input("Enter the x value of your point: "))
                y = int(input("Enter the y value of your point: "))
                print('Your point is ({0},{1}).'.format(x, y))
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
    if f == 1:
        yint = int(input("What is your y-intersept? "))
    elif f == 2:
        print("You do not have enough information to find the equation of the line.")
else:
    print("Do you have at least two points?")
    b = 0
    while b == 0:
        print("yes = 1 no = 2")
        itc = int(input(""))
        if itc == 1:
            b = 1
            q = 0
        elif itc == 2:
            b = 1
            print("You do not have enough information to find the equation of the line.")
            q = 1
        else:
            print("Input unclear, try again.")
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
    rise = y1 - y2
    run = x1 - x2
    m = rise/run
    slv1 = m * x1
    b1 = slv1 - y1
    slv2 = m * x2
    b2 = slv2 - y2
    if b1 == b2:
        yint = b1
    else:
        yint = "ERROR"
    q = 1
if q == 1 or q == 0:
    print('y = {0}x + {1}'.format(m, yint))