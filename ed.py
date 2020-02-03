#Employee data base.
import sys
E = ["Sarah Mullers", "Cassidy Boon", "Derik Sutt", "Eldrige Smith", "Sad Cat"]
c = input("Please input employee number: ")
if int(c) == float(c):
    n = int(c)
else:
    sys.exit()
if n > 4 :
    print(" ")
    print("That is not an employee code")
    print(" ")
    sys.exit()
print(" ")
h = int(input("Please insert hours worked: "))
print(" ")
tax = 0.12
if n == 0:
    bp = 5.80
elif n == 1:
    bp = 6
elif n == 2:
    bp = 8
elif n == 3:
    bp = 4.5
elif n == 4:
    bp = 0
gs = bp * h
ns = gs * tax
print("The take home pay for employee,", E[n], "is $", ns, ".")
print(" ")
e = input("Press Enter to exit.")
sys.exit

    