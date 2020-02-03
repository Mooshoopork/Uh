x = True
while True:
    dy = input("How old is your dog? ")
    try:
        dy = int(dy)
        break
    except:
        print("Please input a whole number. Example: 1, 2, 3")
if dy < 0:
    print("The number is to small to caluclate I'm sorry.")
    x = False
elif dy > 2:
        dy = dy - 2
        age = dy*4
        age = age + 21
elif dy == 2:
    age = 21
elif dy == 1:
    age = 10.5
elif dy == 0:
    age = 0
if x == True:
    age = str(age)
    print("If your dog was human, they would be " + age + " years old.")