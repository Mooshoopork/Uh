echo = "\nTell Me something and I will repeat it."
echo+= "\nEnter 'Quit' to end the program. "

active = True
while active:
    message = input(echo)
    print()
    if message == 'Quit':
        active = False
    else:
        print(message)
        