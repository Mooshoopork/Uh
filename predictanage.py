print("This will predict what age you will be at a certain time.")
start = input("When were you born? ")
end = input("What is the year you want to predict? ")
age = int(end) - int(start)
print("You will be", age)