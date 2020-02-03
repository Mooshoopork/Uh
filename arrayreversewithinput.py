from array import*
print("Input each individual # for your array(x,y,z,a,b,c,q,r)")
while True:
    try:
        x=int(input("x = "))
        y=int(input("y = "))
        z=int(input("z = "))
        a=int(input("a = "))
        b=int(input("b = "))
        c=int(input("c = "))
        q=int(input("q = "))
        r=int(input("r = "))
        break
    except:
        print("NUMBERS ONLY")
anum = array('i', [x, y, z, a, b, c, q, r])
print("In normal order: " + str(anum))
anum.reverse()
print("In reverse order: " + str(anum))
print()
print("The better version.")
anum.reverse()
print('In normal order: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}'.format(anum[0], anum[1], anum[2], anum[3], anum[4], anum[5], anum[6], anum[7]))
anum.reverse()
print('In reverse: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}'.format(anum[0], anum[1], anum[2], anum[3], anum[4], anum[5], anum[6], anum[7]))