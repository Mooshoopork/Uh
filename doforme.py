inp = input("Input: ")
list(inp)
for c in inp:
    if c == inp[0]:
        f = c
    if c == inp[1]:
        t = c
    if c == inp[2]:
        s = c
f = int(f)
s = int(s)
if t == "-":
    awn = f - s
    awn = str(awn)
    print(awn)
if t == "+":
    awn = f + s
    awn = str(awn)
    print(awn)