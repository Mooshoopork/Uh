print("To find the efficence of you vehical please awnser questions below:")
print(" ")
dt = float(input("How far can you travel? "))
ud = input("What is the unit of messurment for the distance you travelled? ")
print(" ")
tv = float(input("How much can you're tank hold? "))
uv = input("What is the unit of mesurment for the volume of your tank? ")
dperv = dt / tv
print(" ")
print("You can drive,", dperv,  ud ,"per one", uv)