import random, math
print("Welcome to the number guessing game. There can be up to 4 players.")
while true:
    pn = int(input("How many players are there? "))
    if pn == 1:
        gametype = 1
        break
    elif pn == 2 or pn == 3 or pn == 4:
        gametype = 2
        break
    else:
        print("Your input was unclear. Please try again.")
if gametype == 1:
    name = input("What is your name? ")
    print(name + ", you have three tries to guess the number between 1 and 20.")
    print("There are three rounds. Good luck.")
    round = 1
    plscore = 0
    compscore = 0
    while round != 4:
        num = random.randint(1, 20)
        count = 0
        while count != 3:
            count = count + 1
            guess = int(input("Take your guess: "))
            if guess == num:
                print("Correct!")
                break
            elif guess > num:
                print("Your guess was too big. Try a smaller number.")
            elif guess < num:
                print("Your guess was too small. Try a bigger number.")
            else:
                print("You've done something seriously wrong my friend.")
        if guess == num:
            count = str(count)
            print("Nice job " + name + "! You guessed the number in " + count + " tries.")
            plscore = plscore + 1   
        elif guess != num:
            num = str(num)
            print("Sorry " + name + ", the number was " + num + ".")
            compscore = compscore + 1
        round = str(round)
        plscore = str(plscore)
        compscore = str(compscore)
        print("End of round " + round + ". " + name + ": " + plscore + " Computer: " + compscore)
        round = int(round)
        round = round + 1
        plscore = int(plscore)
        compscore = int(compscore)
if gametype == 2:
    p1 = input("What is player 1's name? ")
    p2 = input("What is player 2's name? ")
    if pn > 2:
        p3 = input("What is player 3's name? ")
    if pn > 3:
        p4 = input("What is player 4's name? ")
    print("Each player tries to guess the random number between 1 and 20. The person with the closest number recives a point.")
    print("There are five rounds. The person with the most points wins. Good luck.")
    round = 1
    p1s = 0
    p2s = 0
    p3s = 0
    p4s = 0
    while round != 5:
        num = random.randint(1, 20)
        print(p1 + " it's your turn.")
        p1g = int(input("What is your guess? "))
        print(p2 + " it's your turn.")
        s = 2
        while s == 2:
            p2g = int(input("What is your guess? "))
            if p2g == p1g:
                print("Your guess must be diffrent from other guesses. Please guess again.")
            else:
                s = 0
        if pn > 2:
            print(p3 + " it's your turn.")
            s = 2
            while s == 2:
                p3g = int(input("What is your guess? "))
                if p3g == p1g or p3g == p2g:
                    print("Your guess must be diffrent from other guesses. Please guess again.")
                else:
                    s = 0
        if pn > 3:
            print(p4 + " it's your turn.")
            s = 2
            while s == 2:
               p4g = int(input("What is your guess? "))
               if p4g == p1g or p4g == p2g or p4g == p3g:
                   print("Your guess must be diffrent from other guesses. Please guess again.")
               else:
                   s = 0
        if p1g == num:
            p1s = p1s + 1
        elif p2g == num:
            p2s = p2s + 1
        elif pn > 2:
            if pg3 == num:
                p3s = p3s + 1
        elif pn > 3:
            if p4g == num:
                p4s = p4s + 1
        else:
            n1 = math.sqrt((num - p1g)**2)
            n2 = math.sqrt((num - p2g)**2)
            if pn > 2:
                n3 = math.sqrt((num - p3g)**2)
            if pn > 3:
                n4 = math.sqrt((num - p4g)**2)
            if pn == 2:
                if n1 < n2:
                    print("hi")
                    #n1 is closer to num
                elif n2 < n1:
                    print("hi")
                    #n2 is closer to num