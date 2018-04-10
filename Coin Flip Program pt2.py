# count the heads of the simulation

import random

# tracking the number of simulations
simNum=0
flip= random.randint(0,1)
countHeads=0

while simNum<10:
    if flip==1:
        print("head - ", end="")
        countHeads= countHeads+flip
        print(countHeads)
    print(flip)
    flip=random.randint(0,1)
    simNum= simNum+1
