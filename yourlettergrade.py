hg = " "
mg = " "
sg = " "
rg = " "
eg = " "
hgl = " "
mgl = " "
sgl = " "
rgl = " "
egl = " "

while True:
    print()
    print()
    print('Math: {0}, {1}'.format(mg, mgl))
    print('History: {0}, {1}'.format(hg, hgl))
    print('English: {0}, {1}'.format(rg, rgl))
    print('Science: {0}, {1}'.format(sg, sgl))
    print('Elective: {0}, {1}'.format(eg, egl))
    print()
    print("To add a grade, specify which subject.")
    print("If you are done with this section input 'q'.")
    print("1. Math")
    print("2. History")
    print("3. English")
    print("4. Science")
    print("5. Elective")
    choice = input("Choose a subject: 1, 2, 3, 4, or 5 -->  ")
    if choice == "q":
        break
    elif choice == "1":
        type = "math"
        mg = int(input("Please input your " + type + " grade: "))
        if mg <= 100 and mg >= 95:
            mgl = "A+"
        elif mg <= 94 and mg >= 90:
            mgl = "A-"
        elif mg <= 89 and mg >= 85:
            mgl = "B+"
        elif mg <= 84 and mg >= 80:
            mgl = "B-"
        elif mg <= 79 and mg >= 75:
            mgl = "C+"
        elif mg <= 74 and mg >= 70:
            mgl = "C-"
        elif mg <= 69 and mg >= 65:
            mgl = "D+"
        elif mg <= 64 and mg >= 60:
            mgl = "D-"
        elif mg <= 59 and mg >= 55:
            mgl = "F+"
        elif mg <= 54:
            mgl = "F-"
        else:
            mgl = "A++"
    elif choice == "2":
        type = "history"
        hg = int(input("Please input your " + type + " grade: "))
        if hg <= 100 and hg >= 95:
            hgl = "A+"
        elif hg <= 94 and hg >= 90:
            hgl = "A-"
        elif hg <= 89 and hg >= 85:
            hgl = "B+"
        elif hg <= 84 and hg >= 80:
            hgl = "B-"
        elif hg <= 79 and hg >= 75:
            hgl = "C+"
        elif hg <= 74 and hg >= 70:
            hgl = "C-"
        elif hg <= 69 and hg >= 65:
            hgl = "D+"
        elif hg <= 64 and hg >= 60:
            hgl = "D-"
        elif hg <= 59 and hg >= 55:
            hgl = "F+"
        elif hg <= 54:
            hgl = "F-"
        else:
            hgl = "A++"
    elif choice == "3":
        type = "english"
        rg = int(input("Please input your " + type + " grade: "))
        if rg <= 100 and rg >= 95:
            rgl = "A+"
        elif rg <= 94 and rg >= 90:
            rgl = "A-"
        elif rg <= 89 and rg >= 85:
            rgl = "B+"
        elif rg <= 84 and rg >= 80:
            rgl = "B-"
        elif rg <= 79 and rg >= 75:
            rgl = "C+"
        elif rg <= 74 and rg >= 70:
            rgl = "C-"
        elif rg <= 69 and rg >= 65:
            rgl = "D+"
        elif rg <= 64 and rg >= 60:
            rgl = "D-"
        elif rg <= 59 and rg >= 55:
            rgl = "F+"
        elif rg <= 54:
            rgl = "F-"
        else:
            rgl = "A++"
    elif choice == "4":
        type = "science"
        sg = int(input("Please input your " + type + " grade: "))
        if sg <= 100 and sg >= 95:
            sgl = "A+"
        elif sg <= 94 and sg >= 90:
            sgl = "A-"
        elif sg <= 89 and sg >= 85:
            sgl = "B+"
        elif sg <= 84 and sg >= 80:
            sgl = "B-"
        elif sg <= 79 and sg >= 75:
            sgl = "C+"
        elif sg <= 74 and sg >= 70:
            sgl = "C-"
        elif sg <= 69 and sg >= 65:
            sgl = "D+"
        elif sg <= 64 and sg >= 60:
            sgl = "D-"
        elif sg <= 59 and sg >= 55:
            sgl = "F+"
        elif sg <= 54:
            sgl = "F-"
        else:
            sgl = "A++"
    elif choice == "5":
        type = "elective"
        eg = int(input("Please input your " + type + " grade: "))
        if eg <= 100 and eg >= 95:
            egl = "A+"
        elif eg <= 94 and eg >= 90:
            egl = "A-"
        elif eg <= 89 and eg >= 85:
            egl = "B+"
        elif eg <= 84 and eg >= 80:
            egl = "B-"
        elif eg <= 79 and eg >= 75:
            egl = "C+"
        elif eg <= 74 and eg >= 70:
            egl = "C-"
        elif eg <= 69 and eg >= 65:
            egl = "D+"
        elif eg <= 64 and eg >= 60:
            egl = "D-"
        elif eg <= 59 and eg >= 55:
            egl = "F+"
        elif eg <= 54:
            egl = "F-"
        else:
            egl = "A++"
mg = int(mg)
hg = int(hg)
rg = int(rg)
sg = int(sg)
eg = int(eg)
add = mg + hg + rg + sg + eg
ave = add/5
if ave <= 100 and ave >= 95:
    avel = "A+"
elif ave <= 94 and ave >= 90:
    avel = "A-"
elif ave <= 89 and ave >= 85:
    avel = "B+"
elif ave <= 84 and ave >= 80:
    avel = "B-"
elif ave <= 79 and ave >= 75:
    avel = "C+"
elif ave <= 74 and ave >= 70:
    avel = "C-"
elif eg <= 69 and ave >= 65:
    avel = "D+"
elif ave <= 64 and ave >= 60:
    avel = "D-"
elif ave <= 59 and ave >= 55:
    avel = "F+"
elif ave <= 54:
    avel = "F-"
else:
    avel = "A++"
print()
print()
print()
print('Your overal grade is {0} and your letter grade is {1}'.format(ave, avel))