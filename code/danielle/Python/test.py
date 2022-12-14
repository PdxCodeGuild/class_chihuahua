from random import *

dice = []
for x in range(1,6):
    dice.append( randint(1,6) )
    
print(dice)

for x in range(1,6):
    print( dice.count(x) )