while True:
    num = input("What number would you like to multiply? ")
    try:
        num = int(num)
        break
    except:
        print("Please input an integer.")
while True:
    limit = input("What number would you like to go to? ")
    try:
        limit = int(limit)
        break
    except:
        print("Please input an integer.")
count = 0
while count != limit:
    count += 1
    awn = num * count
    print(str(num) + " x " + str(count) + " = " + str(awn))