from array import *
while True:
    def info(x):
        if x == 0:
             print("She is 24 years old.")
             print("She is majoring in political science.")
             print("She has a dog named Ducky.")
             print("Her favorite color is maroon")
             print("She works reception.")
        if x == 1:
             print("He is 18 years old.")
             print("He is in trade school for welding")
             print("He has two goldfish named Rohn and Jerry.")
             print("His favorite color is green")
             print("He is the company's mechanic.")
        if x == 2:
             print("He is 26 years old.")
             print("He is majoring in arctitectual design")
             print("He hates animals.")
             print("His favorite color is mave")
             print("He is the company's designer.")
        if x == 3:
             print("She is 19 years old.")
             print("She is majoring in computer science.")
             print("She has a cat named Carnegy.")
             print("Her favorite color is Purple.")
             print("She works IT.")
        if x == 4 or x == 5 or x == 6 or x == 7 or x == 8 or x == 9:
            print("This slot is still vacant.")
    array_num = array('i', [1,2,3,4,5,6,7,8,9,10])
    list = ['Maya', 'Skeeter', 'John', 'Lele', 'Vacant', 'Vacant', 'Vacant', 'Vacant', 'Vacant', 'Vacant']
    for i in array_num:
        print(str(i) + ". " + list[i-1])
    hi = input("Please enter the number of the person you'd like to see. ")
    put = int(hi) - 1
    print()
    print(list[put] + ":")
    info(put)
    print()
    ag = input("Again? 'yes' or 'no'. ")
    if ag == 'no':
        break