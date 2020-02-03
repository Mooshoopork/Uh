tic = 0
sec = 0
min = 0
hr = 0
day = 0
a = 2
while a == 2:
    while day == 0:
        tic +=1
        if tic == 100000:
            sec +=1
            tic = 0
        if sec == 60:
            min +=1
            sec = 0
        if min == 60:
            hr += 1
            min = 0
        if hr == 24:
            day +=1
            hr = 0
        if tic ==0:
            print("The time is", hr, ":", min, ":", sec)
    print("Good morning!")
    day = 0
