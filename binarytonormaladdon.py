import re
def convo():
    while True:
        i=input("Input a binary number: ")
        if re.search("[10]",i) and not re.search("[23456789]",i)and len(i) == 8:
            break
    x = 1
    number = 0
    hip = list(i)
    hip.reverse()
    for s in hip:
        if s == "1":
            number += x
        x *= 2
    return number
while True:
    q = convo()
    yn = input("Would you like to add another number? 'yes' or 'no': ")
    if yn == "yes":
        u = convo()
        q += u
    else:
        break
print("Your number is", q)