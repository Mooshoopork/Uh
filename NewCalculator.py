import math
#Menu
print("Select an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Square")
print("6. Factorial")
print("7. %ERROR%")
print("8. Prime Detector")
print("9. Area")
print("10. Line Equations")
while True:
    b = 0
    choice = input("Enter choice (1, 2, 3, 4, 5, 6, 7, 8, 9, 10): ")
    if choice == "1":
        print("Your choice is Addition.")
        c = 1
    elif choice == "2":
        print("Your choice is Subtraction.")
        c = 1
    elif choice == "3":
        print("Your choice is Multiplication.")
        c = 1
    elif choice == "4":
        print("Your choice is Division.")
        c = 1
    elif choice == "5":
        print("Your choice is Square.")
        c = 1
    elif choice == "6":
        print("Your choice is Factorial.")
        c = 1
    elif choice == "7":
        print("Your choice is %ERROR%.")
        c = 1
    elif choice == "8":
        print("Your choice is Prime Detector.")
        c = 1
    elif choice == "9":
        print("Your choice is Area.")
        c = 1
    elif choice == "10":
        print("Your choice is Line Equations.")
        c = 1
    else:
        print("Input unclear please try again.")
        c = 0
    if c == 1:
        print("Is this correct?")
        while True:
            print("'yes' or 'no'")
            itc = input()
            if itc == 'yes':
                b = 1
                break
            elif itc == 'no':
                print("Ok, let's try again.")
                b = 0
                break
            else:
                print("Input unclear, try again.")
    if b == 1:
        break
#Start of choice 1-4
if choice == "1" or choice == "2" or choice == "3" or choice == "4":
    while True:
       num1 = input("Please enter your first number: ")
       num2 = input("Please enter your second number: ")
       try:
           num1 = float(num1)
           num2 = float(num2)
           break
       except:
            print()
            print("Only numbers please.")
            print()
    if num1 == int(num1):
        num1 = int(num1)
    if num2 == int(num2):
        num2 = int(num2)
    if choice == "1":
        awn = num1 + num2
        type = "sum"
    elif choice == "2":
        awn = num1 - num2
        type = "diffrence"
    elif choice == "3":
        awn = num1 * num2
        type = "product"
    elif choice == "4":
        while True:
            type = "quotion"
            try:
                awn = num1 / num2
            except:
                print()
                print("Zero gives infinite posiblities and boggles the mind. Please do not divied by zero.")
                print()
                awn = "%ERROR%"
                break
            if awn == int(awn):
                awn = int(awn)
            elif awn == (1/2):
                awn = "1/2"
            elif awn == (1/3):
                awn = "1/3"
            elif awn == (1/4):
                awn = "1/4"
            elif awn == (2/3):
                awn = "2/3"
            elif awn == (3/4):
                awn = "3/4"
            break
    print('The {0} of {1} and {2} is {3}.'.format(type, num1, num2, awn))
#end
#start of chice 5-7
elif choice == "5" or choice == "6" or choice == "7":
    while True:
        num = input("What is your number? ")
        try:
            num = float(num)
            break
        except:
            print()
            print("Only numbers please.")
            print()
    if num == int(num):
        num = int(num)
    if choice == "5":
        type = "square"
        awn = num**2
    elif choice == "6":
        type = "factorial"
        hi = num
        num1 = hi - 1
        num2 = hi * num1
        hi -=1
        a = 0
        while a == 0:
            hi -=1
            if hi != 0:
                num3 = num2 * hi
                num2 = num3
            else:
                a = 1
        awn = num2
    elif choice == "7":
        awn = ("%ERROR%")
    print('The {0} of {1} is {2}.'.format(type, num, awn))
#end
#start of choice 8
elif choice == "8":
    while True:
        num = input("What is your number? ")
        try:
            num = int(num)
            break
        except:
            print()
            print("Only integers please.")
            print()
    t = num / 2
    tt = int(t) * 2
    e = num / 3
    ee = int(e) * 3
    s = num / 5
    ss = int(s) * 5
    k = num / 7
    kk = int(k)* 7
    if num == 2 or num == 3 or num == 5 or num == 7 or num == 1:
        num = 123456
    elif num == 0:
        tt = 4
        ee = 4
        ss = 4
        kk = 4
    if num == tt or num == ee or num == ss or num == kk:
        print("This number isn't prime.")
    elif num == 0:
        print("Are you kidding me -_-")
    else:
        print("This number is prime.")
#end
#Start of choice 9
if choice == '9':
    while True:
        print("What type of area are you calculating?")
        d = input("'3D' or '2D' ")
        if d == '3D' or d == '2D':
            break
        else:
            print("Input unclear. Please try again.")
    if d == '3D':
        while True:
            print("Pick an area type:")
            print("1. Cube")
            print("2. Rectangular Prism")
            form = input()
            if form == "1" or form == "2":
                break
            else:
                print("Input unclear. Please try again.")
#Cube
        if form == '1':
            while True:
                side = input("Input the cube's side length: ")
                try:
                    float(side)
                    break
                except:
                    print("Please enter numbers only.")
            if float(side) == int(side):
                side = int(side)
            else:
                side = float(side)
            awn = side**3
#Rectangular Prism
        elif form == '2':
            while True:
                length = input("Input the length (z side): ")
                wide = input("Input the width (x side): ")
                hight = input("Input the hight (y side): ")
                try:
                    float(length)
                    float(wide)
                    float(hight)
                    break
                except:
                    print("Please enter numbers only.")
            if float(length) == int(length):
                length = int(length)
            else:
                length = float(length)
            if float(wide) == int(wide):
                wide = int(wide)
            else:
                wide = float(wide)
            if float(hight) == int(hight):
                hight = int(hight)
            else:
                hight = float(hight)
            awn = hight*wide*length
    if d == '2D':
        while True:
            print("Pick an area type:")
            print("1. Square")
            print("2. Rectangle")
            form = input()
            if form == "1" or form == "2":
                break
            else:
                print("Input unclear. Please try again.")
#Square
        if form == '1':
            while True:
                side = input("Input the square's side length: ")
                try:
                    float(side)
                    break
                except:
                    print("Please enter numbers only.")
            if float(side) == int(side):
                side = int(side)
            else:
                side = float(side)
            awn = side**2
#Rectangle
        elif form == '2':
            while True:
                wide = input("Input the width (x side): ")
                hight = input("Input the hight (y side): ")
                try:
                    float(wide)
                    float(hight)
                    break
                except:
                    print("Please enter numbers only.")
            if float(wide) == int(wide):
                wide = int(wide)
            else:
                wide = float(wide)
            if float(hight) == int(hight):
                hight = int(hight)
            else:
                hight = float(hight)
            awn = wide*hight
    print("The area is", awn)
#end
#Start of choice 10
#Menu
if choice == "10":
    while True:
        c = 1
        print("What type of line equation would you like to use?")
        print("1. All in one Combo")
        print("2. Slope")
        print("3. Distance")
        print("4. Midpoint")
        lt = input()
        if lt == "1":
            print("Your equation type is All in one Combo")
        elif lt == "2":
            print("Your equation type is Slope")
        elif lt == "3":
            print("Your equation type is Distance")
        elif lt == "4":
            print("Your equation type is Midpoint")
        else:
            print("Input unclear. Please try again.")
            c = 0
            b = 0
        if c == 1:
            print("Is this correct?")
            while True:
                print("'yes' or 'no'")
                itc = input()
                if itc == 'yes':
                    b = 1
                    break
                elif itc == 'no':
                    print("Ok, let's try again.")
                    b = 0
                    break
                else:
                    print("Input unclear, try again.")
        if b == 1:
            break
    fin = 1
    while fin == 1:
#x1 and y1
        while True:
                x1 = input("Enter the x value of your first point: ")
                y1 = input("Enter the y value of your first point: ")
                print('Your first point is ({0},{1}).'.format(x1, y1))
                print("Is this correct?")
                while True:
                    print("'yes' or 'no'")
                    itc = input()
                    if itc == 'yes':
                        b = 1
                        break
                    elif itc == 'no':
                        print("Ok, let's try again.")
                        b = 0
                        break
                    else:
                        print("Input unclear, try again.")
                if b == 1:
                    break
#x2 and y2
        while True:
                x2 = input("Enter the x value of your second point: ")
                y2 = input("Enter the y value of your second point: ")
                print('Your second point is ({0},{1}).'.format(x2, y2))
                print("Is this correct?")
                while True:
                    print("'yes' or 'no'")
                    itc = input()
                    if itc == 'yes':
                        b = 1
                        break
                    elif itc == 'no':
                        print("Ok, let's try again.")
                        b = 0
                        break
                    else:
                        print("Input unclear, try again.")
                if b == 1:
                    break
        fin = 0
#number error check
        try:
            y1 = int(y1)
            y2 = int(y2)
            x1 = int(x1)
            x2 = int(x2)
            rise = y1 - y2
            run = x1 - x2
            m = rise/run
        except:
            print("What you inputed was not numbers, or your denominator is zero. Please try again.")
            fin = 1
#Etra math needed
    if m == int(m):
        m = int(m)
    mx = (x1 + x2)/2
    my = (y1 + y2)/2
    if mx == int(mx):
        mx = int(mx)
    if my == int(my):
        my = int(my)
    d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    print()
    print()
    d = str(d)
    m = str(m)
    if lt == "1":
        print("The slope is " + m + ".")
        print("The distance of the line is " + d + ".")
        print('The midpoint is ({0},{1}).'.format(mx, my))
    elif lt == '2':
        print("The slope is " + m + ".")
    elif lt == '3':
        print("The distance of the line is " + d + ".")
    elif lt == '4':
        print('The midpoint is ({0},{1}).'.format(mx, my))