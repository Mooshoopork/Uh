s = input("Write something: ")
d=l=o=n=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    elif c=='!' or c=='@' or c=='#' or c=='$' or c=='%' or c=='^' or c=='&' or c=='*' or c=='(' or c==')':
        o=o+1
    else:
        n=n+1
print("The amount of letters is" , l)
print("The amount of digits is", d)
print("The amount of asinged symbols is", o)
print("The amount of non digits/letters/asinged symbols is", n)