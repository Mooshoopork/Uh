while True:
    mon = True
    while mon:
        print("The months of the year: January, February, March, April, May, June, July, August, September, October, November, and December")
        month = input("Input month: ")
        if month == "q" or month == "January" or month == "February" or month == "March" or month == "April" or month == "May" or month == "June" or month == "July" or month == "August" or month == "September" or month == "October" or month == "November" or month == "December":
            mon = False
        else:
            print()
            print("Make sure the months are spelt correctly, capitalized, and do in fact exist.")
            print()
    if month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "December":
        ma = "31"
    if month == "February":
        ma = "28/29"
    if month == "April" or month == "June" or month == "September" or month == "November":
        ma = "30"
    if month == "q":
        break
    print()
    print("The number of days is " + ma + ".")
    print()