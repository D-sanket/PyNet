from random import random


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

    def getData(self):
        return self.data
