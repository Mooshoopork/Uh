#Passcode
import re
p = input("Input your passcode here: ")
x = True

while x:
    if (len(p)<6 or len(p)>20):
        l = " the length is between 6 and 20 characters."
        break
    elif not re.search("[a-z]",p):
        l = " there is a lowercase letter charecter."
        break
    elif not re.search("[0-9]",p):
        l = " there is a number charecter."
        break
    elif not re.search("[A-Z]",p):
        l = " there is an uppercase letter charecter."
        break
    elif not re.search("[!@#$%^&*()]",p):
       l = " there is a special charecter."
       break
    elif re.search("\s",p):
        l = " there is NO \s."
        break
    else:
        print("Valid Passcode")
        x = False
        break
if x:
    print("Not a Valid Passcode")
    print("Please make sure", l)