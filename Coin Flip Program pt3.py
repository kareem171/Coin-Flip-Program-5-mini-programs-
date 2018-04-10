# simulation terminates once you have 5 heads


import random


#tracking the number of simulations until you have 5 heads

simNum=0
countHeads=0
flip= random.randint(0,1)


while countHeads<5:
    flip= random.randint(0,1)
    if flip==1:
        countHeads=countHeads+flip
    print(flip)
    print("Heads =", countHeads)
    simNum=simNum+1


print("Total flips",simNum)
