from random import random

from Helper import sigmoid, sigmoidPrime


class Neuron:

    def __init__(self, numWeights):
        self.data = random()
        self.weights = []
        self.bias = random()
        self.numWeights = numWeights

        for weightNum in range(numWeights):
            weight = random()
            self.weights.append(weight)

    def setData(self, data):
        self.data = data

    def setBias(self, bias):
        self.bias = bias

    def setWeight(self, index, weight):
        self.weights[index] = weight

    def getData(self):
        return self.data

    def getBias(self):
        return self.bias

    def getWeight(self, index):
        return self.weights[index]

    def activate(self):
        self.data = sigmoid(self.data)

    def deactivate(self):
        self.data = sigmoidPrime(self.data)
