#prime number detector
num = int(input("Please enter your number: "))
print("")
print('The number you chose was {0}.'.format(num))
t = num / 2
tt = int(t) * 2
e = num / 3
ee = int(e) * 3
s = num / 5
ss = int(s) * 5
k = num / 7
kk = int(k)* 7
if num == 2 or num == 3 or num == 5 or num == 7 or num == 1:
    num = 123456
if num == tt or num == ee or num == ss or num == kk:
    print("This number isn't prime.")
elif num == 0:
    print("Are you kidding me -_-")
else:
    print("This number is prime.")
    