import re
x = True
while x:
    i=input("Input 8 charecter binary number: ")
    if len(i) == 8:
        x = False
    if not re.search("[10]",i):
        x = True
if i[7] == "0":
    ones = 0
elif i[7] == "1":
    ones = 1
if i[6] == "0":
    twos = 0
elif i[6] == "1":
    twos = 2
if i[5] == "0":
    threes = 0
elif i[5] == "1":
    threes = 4
if i[4] == "0":
    fours = 0
elif i[4] == "1":
    fours = 8
if i[3] == "0":
    fives = 0
elif i[3] == "1":
    fives = 16
if i[2] == "0":
    sixes = 0
elif i[2] == "1":
    sixes = 32
if i[1] == "0":
    sevens = 0
elif i[1] == "1":
    sevens = 64
if i[0] == "0":
    eights = 0
elif i[0] == "1":
    eights = 128
number = ones+twos+threes+fours+fives+sixes+sevens+eights
print(number)