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

    def prevLayer(self):
        return self.net.getLayer(self.index-1)


    def setData(self, data):
        if len(data) != self.length:
            print("Wrong data supplied!")
            sys.exit(0)

        for neuronNum in range(self.length):
            self.neurons[neuronNum].setData(data[neuronNum])

    def getNeuron(self, index):
        return self.neurons[index]

    def getNeurons(self):
        return self.neurons

    def print(self):
        dataString = "["
        for neuronNum in range(self.length):
            dataString += str(self.neurons[neuronNum].getData())+" "
        dataString = dataString[:-1]+"]"
        print(dataString)

    def feedForward(self):
        nxtLayer = self.nextLayer()

        if nxtLayer is None:
            for neuronNum in range(self.length):
                neuron = self.getNeuron(neuronNum)
                neuron.activate()
            return

        nxtLayerData = []

        for nxtNeuronNum in range(nxtLayer.length):
            data = 0
            for neuronNum in range(self.length):
                neuron = self.getNeuron(neuronNum)
                neuron.activate()
                data += neuron.getData() * neuron.getWeight(nxtNeuronNum)

            data += nxtLayer.getNeuron(nxtNeuronNum).getBias()

            nxtLayerData += [data]

        nxtLayer.setData(nxtLayerData)
