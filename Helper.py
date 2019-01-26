import math


def sigmoid(x):
    return 1/(1+math.exp(-x))

def sigmoidPrime(x):
    return x*(1-x)
