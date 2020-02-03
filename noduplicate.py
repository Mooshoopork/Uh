def td(array_nums):
    numset = set(array_nums)
    return len(array_nums) != len(numset)
try:
    print("Unfortunatly, this program only compares single charecters.")
    array=input("Input your array without commas here: ")
    print()
    print("Is there duplicates in this list?")
    print(td(list(array)))
except:
    print()
    print("I don't know. I hounestly don't know what went wrong so good luck figuring it out.")