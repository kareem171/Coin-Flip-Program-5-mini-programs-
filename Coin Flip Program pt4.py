# 1000 heads in your simulation


import random


#tracking the number of simulations until you have 1000 heads

simNum=0
countHeads=0
flip= random.randint(0,1)


while countHeads<1000:
    flip= random.randint(0,1)
    if flip==1:
        countHeads=countHeads+flip
    print(flip)
    print("Heads =", countHeads)
    simNum=simNum+1


print("Total flips",simNum)
