n = input("Hi! Nice to meet you! What is your name?: ")
print(" ")
if n == "Jen":
    print(n ,"? We have the same name!")
    print(" ")
    q = true
    g = input("I assume you're a girl, right? ")
    if g == "yes":
        g = "f"
    elif g == "y":
        g = "f"
    elif g == "right":
        g = "f"
    elif g == "Right":
        g = "f"
    elif g == "Yes":
        g = "f"
    elif g == "Y":
        g = "f"
    elif g == "yep":
        g = "f"
    elif g == "Yep":
        g = "f"
    else:
        g = input("Are you a boy? ")
        if g == "yes":
                g = "m"
        elif g == "y":
                g = "m"
        elif g == "yeah":
                g = "m"
        elif g == "Yeah":
                g = "m"
        elif g == "Yes":
                g = "m"
        elif g == "Y":
                g = "m"
        else:
                g = "a"
else:
    print("Hi,", n ,"! I am Jen!")
    print(" ")
    q = false
    g = input("Are you a girl or boy? ")
    if g == "girl":
        g = "f"
    elif g == "Girl":
        g = "f"
    elif g == "boy":
        g = "m"
    elif g == "Boy":
        g = "m"
    else:
        g = "a"
print(" ")
age = int(input("How old are you? As a digit please: "))
    if age == 15 and g == "f":
        if q == false:
            jen = input("Are you sure you're name isn't Jen? ")