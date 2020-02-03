#Hang Man
sry = "Sorry, try again."
st = "_"
nd = "_"
rd = "_"
oth = "_"
fth = "_"
ith = "_"
sth = "_"
eth = "_"
life = 9
a = "A"
b = "B"
c = "C"
d = "D"
e = "E"
f = "F"
g = "G"
h = "H"
i = "I"
j = "J"
k = "K"
l = "L"
m = "M"
n = "N"
o = "O"
p = "P"
q = "Q"
r = "R"
s = "S"
t = "T"
u = "U"
v = "V"
w = "W"
x = "X"
y = "Y"
z = "Z"
while True:
    print()
    print("Lives: ", str(life))
    print(a, b, c, d, e, f, g, h, i, j, k, l)
    print(m, n, o, p, q, r, s, t, u, v, w, x, y, z)
    print()
    print(st, " ", nd, rd, oth, fth, " ", ith, sth, eth)
    print()
    if life == 0:
        phrase = "I'm sorry,"
        break
    elif st != "_" and nd != "_" and rd != "_" and oth != "_" and fth != "_" and ith != "_" and sth != "_" and eth != "_":
        phrase = "Congratulations,"
        break
    guess = input("Guess the phrase! Input a letter: ")
    if guess == "I" and i == "I" or guess == "i" and i == "I":
       st = "I"
       i = ""
       print()
       input("Nice")
    elif guess == "l" and l == "L" or guess == "L" and l == "L":
        nd = "l"
        l = ""
        print()
        input("Nice")
    elif guess == "O" and o == "O" or guess == "o" and o == "O":
        rd = "o"
        sth = "o"
        o = ""
        print()
        input("Nice")
    elif guess == "v" and v == "V" or guess == "V" and v == "V":
        oth = "v"
        v = ""
        print()
        input("Nice")
    elif guess == "e" and e == "E" or guess == "E" and e == "E":
        fth = "e"
        e = ""
        print()
        input("Nice")
    elif guess == "y" and y == "Y" or guess == "Y" and y == "Y":
        ith = "y"
        y = ""
        print()
        input("Nice")
    elif guess == "u" and u == "U" or guess == "U" and u == "U":
        eth = "u"
        u = ""
        print()
        input("Nice")
    elif guess == "a" and a == "A" or guess == "A" and a == "A":
        a = ""
        print()
        input(sry)
        life -= 1
    elif guess == "b" and b == "B" or guess == "B" and b == "B":
        b = ""
        print()
        input(sry)
        life -= 1
    elif guess == "c" and c == "C" or guess == "C" and c == "C":
        c = ""
        print()
        input(sry)
        life -= 1
    elif guess == "d" and d == "D" or guess == "D" and d == "D":
        d = ""
        print()
        input(sry)
        life -= 1
    elif guess == "f" and f == "F" or guess == "F" and f == "F":
        f = ""
        print()
        input(sry)
        life -= 1
    elif guess == "g" and g == "G" or guess == "G" and g == "G":
        g = ""
        print()
        input(sry)
        life -= 1
    elif guess == "h" and h == "H" or guess == "H" and h == "H":
        h = ""
        print()
        input(sry)
        life -= 1
    elif guess == "j" and j == "J" or guess == "J" and j == "J":
        j = ""
        print()
        input(sry)
        life -= 1
    elif guess == "k" and k == "K" or guess == "K" and k == "K":
        k = ""
        print()
        input(sry)
        life -= 1
    elif guess == "m" and m == "M" or guess == "M" and m == "M":
        m = ""
        print()
        input(sry)
        life -= 1
    elif guess == "n" and n == "N" or guess == "N" and n == "N":
        n = ""
        print()
        input(sry)
        life -= 1
    elif guess == "p" and p == "P" or guess == "P" and p == "P":
        p = ""
        print()
        input(sry)
        life -= 1
    elif guess == "q" and q == "Q" or guess == "Q" and q == "Q":
        q = ""
        print()
        input(sry)
        life -= 1
    elif guess == "r" and r == "R" or guess == "R" and r == "R":
        r = ""
        print()
        input(sry)
        life -= 1
    elif guess == "s" and s == "S" or guess == "S" and s == "S":
        s = ""
        print()
        input(sry)
        life -= 1
    elif guess == "t" and t == "T" or guess == "T" and t == "T":
        t = ""
        print()
        input(sry)
        life -= 1
    elif guess == "w" and w == "W" or guess == "W" and w == "W":
        w = ""
        print()
        input(sry)
        life -= 1
    elif guess == "x" and x == "X" or guess == "X" and x == "X":
        x = ""
        print()
        input(sry)
        life -= 1
    elif guess == "z" and z == "Z" or guess == "Z" and z == "Z":
        z = ""
        print()
        input(sry)
        life -= 1
    else:
        print()
        input("Please only enter one letter at a time, and make sure not to repeat letters.")
print()
print(phrase, "the phrase was 'I love you'.")