# simulate a coin flip 10 times



import random

#track the number of simulations
# 1= head, 0= tails

simNum = 0
flip = random.randint(0,1)

while simNum<10:
    print(flip)
    flip= random.randint(0,1)
    simNum=simNum+1

print("10 times done")
