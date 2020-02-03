import sys

def compare(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == "rock":
        if u2 == 'scissors':
            return("Rock beats scissors!")
        else:
            return("Paper beats rock!")
    elif u1 == "scissors":
        if u2 == 'paper':
            return("Scissors beat paper!")
        else:
            return("Rock beats scissors!")
    elif u1 == "paper":
        if u2 == 'rock':
            return("Rock beats scissors!")
        else:
            return("Scissors beat paper!")

print("Hello and welcome to rock, paper, scissors!")

user1=input("What's your name, friend? ")
print("Nice to meet you, " + user1)
user2=input("And whats your name, friend? ")
print("It's nice to meet you too, " + user2)
x = True
y = True
while x:
    awn1=input("%s, choose your fighter! Rock, paper, or scissors? " % user1)
    if awn1 == "rock" or awn1 == "paper" or awn1 == "scissors":
        x = False
    else:
        print("Please input a valid choice. Also make sure the choice is not capitalised.")
while y:
    awn2=input("%s, choose your fighter! Rock, paper, or scissors? " % user2)
    if awn2 == "rock" or awn2 == "paper" or awn2 == "scissors":
        y = False
    else:
        print("Please input a valid choice. Also make sure the choice is not capitalised.")
print("Now fight!")
print(user1 + " chose " + awn1)
print(user2 + " chose " + awn2)
print(compare(awn1, awn2))