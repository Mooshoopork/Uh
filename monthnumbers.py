mon = True
da = True
while mon:
    print("The months of the year: January, February, March, April, May, June, July, August, September, October, November, and December")
    month = input("What month is it? ")
    if month == "January" or month == "February" or month == "March" or month == "April" or month == "May" or month == "June" or month == "July" or month == "August" or month == "September" or month == "October" or month == "November" or month == "December":
        mon = False
    else:
        print()
        print("Make sure the months are spelt correctly, capitalized, and do in fact exist.")
        print()
if month == "February":
    lea = True
else:
    lea = False
while lea:
    leap = input("Is it a leap year, 'yes' or 'no'? ")
    if leap == "yes" or leap == "no":
        lea = False
    else:
        print()
        print("Please awnser with a lower case 'yes' or 'no'.")
        print()
if month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "December":
    ma = 31
if month == "February":
    if leap == "yes":
        ma = 29
    else:
        ma = 28
if month == "April" or month == "June" or month == "September" or month == "November":
    ma = 30
while da:
    day = input("What day are you on? ")
    try:
        day = int(day)
        if day <= ma and day > 0:
            da = False
        else:
            print()
            print("Please enter a numeral value that makes sense.")
            print()
    except:
        print()
        print("Please enter numbers.")
        print()
day=str(day)
ma = str(ma)
print("You are on day " + day + "/" + ma + ".")