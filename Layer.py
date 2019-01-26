import sys

from Neuron import Neuron


class Layer:

    def __init__(self, numNeurons, numNeuronsNext, index, net):
        self.length = numNeurons
        self.index = index
        self.net = net

        self.neurons = []

        for neuronNum in range(numNeurons):
            neuron = Neuron(numNeuronsNext)
            self.neurons.append(neuron)

    def nextLayer(self):
        return self.net.getLayer(self.index+1)


    def setData(self, data):
        if len(data) != self.length:
            print("Wrong data supplied!")
            sys.exit(0)

        for neuronNum in range(self.length):
            self.neurons[neuronNum].setData(data[neuronNum])

    def print(self):
        for neuronNum in range(self.length):
            print(str(self.neurons[neuronNum].getData())+" ")
