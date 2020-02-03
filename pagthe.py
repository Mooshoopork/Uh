import math
while 1 == 1:
    print()
    print("This program calculates the missing side of a triangle. If you'd like to quit press q")
    print("Are you looking for the hypotenuse or a leg?")
    prob = input("hyp or leg: ")
    if prob == "hyp":
        a = int(input("What is the value of your first leg? "))
        b = int(input("What is the value of your second leg? "))
        aa = a**2
        bb = b**2
        hh = aa + bb
        h = math.sqrt(hh)
        if h == int(h):
            h = int(h)
            h = str(h)
        else:
            q = str(h)
            hh = str(hh)
            h = q + " or the square root of " + hh
        print()
        print("The hypotinuse is " + h + ".")
        print()
        print()
        con = input("Press enter to continue...")
    elif prob == "leg":
        h = int(input("What is the value of your hypotenuse? "))
        a = int(input("What is the value of your leg? "))
        if h > a:
            aa = a**2
            hh = h**2
            bb = hh - aa
            b = math.sqrt(bb)
            if b == int(b):
                b = int(b)
                b = str(b)
            else:
                q = str(b)
                bb = str(bb)
                b = q + " or the square root of " + bb
            print()
            print("The missing leg is " + b + ".")
            print()
            print()
            con = input("Press enter to continue...")
        else:
            print()
            print("Something went wrong. Please make sure you are using the right type of equations and that your values are correct.")
            print()
            print()
            con = input("Press enter to continue...")
    elif prob == "q":
        break
    else:
        print()
        print("You need to pay a little more attention. Please enter a listed answer, or press q to quit.")
        print()
        print()
        con = input("Press enter to continue...")