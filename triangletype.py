#figure out if a triangle is equalateral scalene or isosleces
def e():
    print(" ^")
    print("/ \\")
    print("---")
def s():
    print(" /|")
    print("/ |")
    print("--")
def i():
    print(" ^")
    print("/ |")
    print("\ |")
    print(" \|")
tri = "\nEnter your triangle side length: "
yorn = "\nIs this correct?"
yorn += "\n'yes' or 'no' "
while True:
    a = 0
    print()
    print("For your first side.")
    s1 = input(tri)
    try:
        float(s1)
    except:
        print("Try again! Only numbers please.")
        a = 1
    if a == 0:
        print("The side is " + s1)
        yn=input(yorn)
        if yn == 'yes':
            break
while True:
    a = 0
    print()
    print("For your second side.")
    s2 = input(tri)
    try:
        float(s1)
    except:
        print("Try again! Only numbers please.")
        a = 1
    if a == 0:
        print("The side is " + s2)
        yn=input(yorn)
        if yn == 'yes':
            break
while True:
    a = 0
    print()
    print("For your third side.")
    s3 = input(tri)
    try:
        float(s1)
    except:
        print("Try again! Only numbers please.")
        a = 1
    if a == 0:
        print("The side is " + s3)
        yn=input(yorn)
        if yn == 'yes':
            break
if s1 == s2 and s1 == s3:
    print("The triangle is equalateral.")
    e()
elif s1 == s2 or s1 == s3:
    print("The triangle is isosoleaces.")
    s()
elif s2 == s3:
    print("The triangle is isosoleaces.")
    s()
else:
    print("The triangle is scalean.")
    i()