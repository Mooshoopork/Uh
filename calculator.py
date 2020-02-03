#menu
import math
print("Select an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Square")
print("6. Factorial")
print("7.")
print("8. Prime Detector")
print("9. Area")
print("10. Line Equations")
c = 0
while c == 0:
    choice = input("Enter choice (1, 2, 3, 4, 5, 6, 7, 8, 9, 10): ")

#Calculator
    if choice == "1" or choice == "2" or choice == "3" or choice == "4":
        c = 1
        num1 = float(input("Please enter your first number: "))
        num2 = float(input("Please enter your second number: "))
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
            awn = num1 / num2
            type = "quotion"
        if awn == int(awn):
            awn = int(awn)
        print('The {0} of {1} and {2} is {3}.'.format(type, num1, num2, awn))
    elif choice == "5" or choice == "6" or choice == "7" or choice == "8":
        c = 1
        num = int(input("Please enter your number: "))
        if choice == "5":
            awn = num * num
            print('The square of {0} is {1}'.format(num, awn))
        elif choice == "6":
            a = 0
            hi = num
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
            print('The factorial of {0} is {1}'.format(hi, num2))
        elif choice == "7":
            a = 0
            hi = num
            num1 = num - 1
            num2 = num + num1
            num -=1
            while a == 0:
                num -=1
                if num != 0:
                    num3 = num2 + num
                    num2 = num3
                else:
                    print(hi)
        elif choice == "8":
            print('The number you chose was {0}.'.format(num))
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
            if num == tt or num == ee or num == ss or num == kk:
                print("This number isn't prime.")
            elif num == 0:
                print("Are you kidding me -_-")
            else:
                print("This number is prime.")
    elif choice == "9":
        c = 1
        print("Area Types:")
        print("1. Square/Rectangle")
        print("2. Cube/Rectangular Prism")
        type = int(input("What type of area would you like to calculate? (1, 2...) "))
        if type == 1:
            x = 0
            while x == 0:
                print("1 = Square or 2 = Rectangle")
                sor = int(input("Which one? "))
                if sor == 1:
                    x = 1
                    t = "square"
                    side = int(input("What is the lenght of it's sides? "))
                    area = side * side
                    s1 = side
                    s2 = side
                elif sor == 2:
                    x = 1
                    t = "rectangle"
                    s1 = int(input("What is the rectangle's lenght? "))
                    s2 = int(input("What is the rectangle's width? "))
                    area = s1 * s2
                else:
                    print("Choice unclear, try again.")
            print('The {0} with the dimentions'.format(t))
            if type == 1:
                print('L = {0} W = {1}'.format(s1, s2))
            print('has an area of {0}'.format(area))
        elif type == 2:
            x = 0
            while x == 0:
                print("1 = Cube or 2 = Rectangular prism")
                sor = int(input("Which one? "))
                if sor == 1:
                   x = 1
                   t = "cube"
                   side = int(input("What is the lenght of it's sides? "))
                   s1 = side
                   s2 = side
                   s3 = side
                   volume = s1 * s2 * s3
                elif sor == 2:
                    x = 1
                    t = "rectangular prism"
                    s1 = int(input("What is the rectangular prism's lenght? "))
                    s2 = int(input("What is the rectangular prism's width? "))
                    s3 = int(input("What is the rectangular prism's hight? "))    
                    volume = s1 * s2 * s3
                else:
                    print("Choice unclear, try again.")
            print('The {0} with the dimentions'.format(t))
            if type == 1:
                print('L = {0} W = {1} H = {s3}'.format(s1, s2, s3))
            print('has an area of {0}'.format(volume))
        
    elif choice == "10":
        c = 1
        print("Which equation would you like to use?")
        print("1. All in one Combo")
        print("2. Slope")
        print("3. Distance")
        print("4. Midpoint")
        type = int(input())
        w = 0
        while w == 0:
            x1 = int(input("Enter the x value of your first point: "))
            y1 = int(input("Enter the y value of your first point: "))
            print('Your first point is ({0},{1}).'.format(x1, y1))
            print("Is this correct?")
            b = 0
            while b == 0:
                print("yes = 1 no = 2")
                itc = input()
                if itc == "1":
                    b = 1
                    w = 1
                elif itc == "2":
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
                itc = input(" ")
                if itc == "1":
                    b = 1
                    w = 1
                elif itc == "2":
                    b = 1
                    print("Ok, let's try again.")
                else:
                    print("Input unclear, try again.")
        rise = y1 - y2
        run = x1 - x2
        if run != 0:
            m = rise/run
        else:
            m = 0
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
        if type == 1:
            print("The slope is " + m + ".")
            print("The distance of the line is " + d + ".")
            print('The midpoint is ({0},{1}).'.format(mx, my))
        elif type == 2:
            print("The slope is " + m + ".")
        elif type == 3:
           print("The distance of the line is " + d + ".") 
        elif type == 4:
            print('The midpoint is ({0},{1}).'.format(mx, my))
    else:
        print()
        print("Choice not defined. Try again.")
        print()
 