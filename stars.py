space = ['', ' ', '  ', '   ', '    ', '     ', '      ', '       ', '        ', '          ', '          ']
star = '*'
count = 2
while True:
    stars=input("How many stars on the line? ")
    spaces=input("How many spaces in between? ")
    try:
        stars=int(stars)
        int(spaces)
        break
    except:
        pass
if int(spaces) > 10 and int(spaces) < 100:
    