from mcpi import minecraft
def Print(x):
    mc.postToChat(x)
mc = minecraft.Minecraft.create()
Print(input("What do you want to say? "))