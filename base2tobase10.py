import re
while True:
    i=input("Input a number in base two: ")
    if re.search("[10]",i) and not re.search("[23456789]",i):
        break
x = 1
number = 0
hip = list(i)
hip.reverse()
for s in hip:
    if s == "1":
        number += x
    x *= 2
print("The number in base ten is: ", number)