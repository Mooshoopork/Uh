from array import *
anum = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
print("In normal order: " + str(anum))
anum.reverse()
print("In reverse order: " + str(anum))
print()
print("The better version.")
anum.reverse()
print('In normal order: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}'.format(anum[0], anum[1], anum[2], anum[3], anum[4], anum[5], anum[6], anum[7]))
anum.reverse()
print('In reverse: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}'.format(anum[0], anum[1], anum[2], anum[3], anum[4], anum[5], anum[6], anum[7]))