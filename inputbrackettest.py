import re
while True:
    word = input("Whats the word? ")
    if not re.search("[0-9]",word):
        break
    else:
        print("No numbers please!")
sqb = ""
for s in word:
    if re.search("[a-z]",s):
        sqb += "_"
        sqb+=" "
    elif re.search("[A-Z]",s):
        sqb+="_"
        sqb+=" "
    else:
        sqb+=s
        sqb+=" "
print(sqb)
while True:
    guess = input(": ")
    if re.search(guess, word):
        print(guess)