print("Enter 'Quit' to end the program.")
name = "\nWhat is your name? "
bday = "\nAlso when were you born?"
bday += "\nExamples monthyear = 072002: "
dat = "\nWhat year is it?"
dat += "\nExample monthyear = 112019: "
gen = "\n are you a 'boy' or 'girl'? "
while True:
    person = input(name)
    if person == 'Quit':
        break
    sex = input(gen)
    if sex == 'Quit':
        break
    elif sex == 'boy':
        sex = "he"
    elif sex == 'girl':
        sex = "she"
    birthday = input(bday)
    if birthday == 'Quit':
        break
    date = input(dat)
    if date == 'Quit':
        break
    print()
    for c in birthday:
        try:
            bmon1 = birthday[0]
            bmon2 = birthday[1]
            bmonth = bmon1 + bmon2
            bmonthint = int(bmonth)
            byear1 = birthday[2]
            byear2 = birthday[3]
            byear3 = birthday[4]
            byear4 = birthday[5]
            byear = byear1 + byear2 + byear3 + byear4
            byearint = int(byear)
        except:
            print("You must input 6 numbers in mmyyyy order for the system to work. Please start over.")
            break
    for c in date:
        try:
            dmon1 = date[0]
            dmon2 = date[1]
            dmonth = dmon1 + dmon2
            dmonthint = int(dmonth)
            dyear1 = date[2]
            dyear2 = date[3]
            dyear3 = date[4]
            dyear4 = date[5]
            dyear = dyear1 + dyear2 + dyear3 + dyear4
            dyearint = int(dyear)
        except:
            print("You must input 6 numbers in mmyyyy order for the system to work. Please start over.")
            break
    if bmonth == "01":
        bmonth = "January"
    elif bmonth == "02":
        bmonth = "Febuary"
    elif bmonth == "03":
        bmonth = "March"
    elif bmonth == "04":
        bmonth = "April"
    elif bmonth == "05":
        bmonth = "May"
    elif bmonth == "06":
        bmonth = "June"
    elif bmonth == "07":
        bmonth = "July"
    elif bmonth == "08":
        bmonth = "August"
    elif bmonth == "09":
        bmonth = "September"
    elif bmonth == "10":
        bmonth = "October"
    elif bmonth == "11":
        bmonth = "November"
    elif bmonth == "12":
        bmonth = "December"
    else:
        print("The date was sumitted incorectly. Please try again.")
        break
    if dmonth == "01":
        dmonth = "January"
    elif dmonth == "02":
        dmonth = "Febuary"
    elif dmonth == "03":
        dmonth = "March"
    elif dmonth == "04":
        dmonth = "April"
    elif dmonth == "05":
        dmonth = "May"
    elif dmonth == "06":
        dmonth = "June"
    elif dmonth == "07":
        dmonth = "July"
    elif dmonth == "08":
        dmonth = "August"
    elif dmonth == "09":
        dmonth = "September"
    elif dmonth == "10":
        dmonth = "October"
    elif dmonth == "11":
        dmonth = "November"
    elif dmonth == "12":
        dmonth = "December"
    else:
        print("The date was sumitted incorectly. Please try again.")
        break
    age = dyearint - byearint
    if bmonthint > dmonthint:
        age = age - 1
    age = str(age)
    print(person + " is " + age + " because " + sex + " was born in " + bmonth + " and the month is " + dmonth + ".")