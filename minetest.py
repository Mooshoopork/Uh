from mcpi import minecraft
def Print(x):
    mc.postToChat(x)
while True:
    mc = minecraft.Minecraft.create()
    pos = mc.player.getPos()
    Print(pos)
    Print("Hi Gianna")
    Print(input("Type something"))