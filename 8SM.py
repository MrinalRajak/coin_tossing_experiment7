

# 8:Find the probability of having 2 heads out of 10 coins tossed.
# (Answer should be first analitically calculated and then numerically
# verified).


import numpy as np
import math
import random
from numpy.random import randint


def count2exacthead(tosses):
    Coin = ['H','T']
    Toss = []
    Head = 0
    Probability = 0
    for i in range(tosses):
        Toss.append(random.choice(Coin))

    for i in Toss:
        if i == 'H':
            Head += 1
    if Head == 2:
        Probability += 1
    return Probability
for i in range(5):
    experiments = 1000
    AvgProbability = 0
    for i in range(experiments):
        AvgProbability += count2exacthead(10)
    AvgProbability /= float(experiments)
print("Exprimentally calculated Probability: ",AvgProbability)


def analitical():
    successes = 0
    for k in range (11):
        successes += (math.factorial(10)/(math.factorial(2)*math.factorial(10-2)))*(0.5)**2*(0.5)**8
    possible_heads = 10
    return successes/float(possible_heads)

print("Analitically calculated Probability: ",analitical())
        
        
    
