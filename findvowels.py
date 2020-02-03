#find vowels
def ae(x):
    if x == "a" or x == "e" or x== "i" or x== "o" or x == "u":
        return True
stuff = input("Type some words: ")
for c in stuff:
    if ae(c):
        print(c)