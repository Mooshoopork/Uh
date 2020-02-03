l = ['*', '**', '***', '****', '*****']
count = 0
y = 0
while True:
    print(l[count])
    if count == 0 and y == 1:
        break
    if count < 4 and y == 0:
        count +=1
    elif count == 4:
        count -=1
        y = 1
    elif count >= 0 and y == 1:
        count -=1
    
