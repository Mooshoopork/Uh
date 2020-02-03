#Mutiplication table from 1-10
while True:
    num = input("What number would you like to multiply? ")
    try:
        num = int(num)
        break
    except:
        print("Please input an integer.")
print("Here is the multiplication table:")
awn = num * 1
print(str(num) + " x 1 = " + str(awn))
awn = num * 2
print(str(num) + " x 2 = " + str(awn))
awn = num * 3
print(str(num) + " x 3 = " + str(awn))
awn = num * 4
print(str(num) + " x 4 = " + str(awn))
awn = num * 5
print(str(num) + " x 5 = " + str(awn))
awn = num * 6
print(str(num) + " x 6 = " + str(awn))
awn = num * 7
print(str(num) + " x 7 = " + str(awn))
awn = num * 8
print(str(num) + " x 8 = " + str(awn))
awn = num * 9
print(str(num) + " x 9 = " + str(awn))
awn = num * 10
print(str(num) + " x 10 = " + str(awn))