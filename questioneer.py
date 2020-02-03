import sys
print("This is a questioneer about the programer.")
print("Please awnser with numeric values.")
print(" ")
num = input("What is my favorit number? ")
print(" ")
if float(num) == 5:
    print("Correct")
    print(" ")
    year = input("What year is it? ")
    print(" ")
    age = input("How old am I? ")
    print(" ")
    aget = int(year) - 2002
    agea = int(age)
    if agea == aget:
        print("Correct")
        print(" ")
        if int(year) == 2019:
            print("Bounus Question!")
            cat = input("How many cats do I have? ")
            print(" ")
            if int(cat) == 7:
                print("Correct")
                print("Good bye.")
                print(" ")
            else:
                print("Wrong")
                print(" ")
        else:
            print("Good bye.")
            print(" ")
    else:
        print("Wrong")
        print(" ")
else:
    print("Wrong")
    print(" ")