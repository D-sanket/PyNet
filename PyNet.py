import sys
from math import floor
from random import shuffle

import Helper
from Matrix import Matrix


class PyNet:

    def __init__(self, structure, learningRate = 0.1):
        self.structure = structure
        self.learningRate = learningRate
        self.layers = []
        self.weights = {}
        self.biases = {}
        self.errors = {}
        self.numLayers = len(structure)
        for layerNum in range(self.numLayers):
            layer = Matrix(structure[layerNum], 1).randomize()
            self.layers.append(layer)

        for layerNum in range(self.numLayers-1):
            currentLayer = self.layers[layerNum]
            nextLayer = self.layers[layerNum+1]
            self.weights[layerNum] = {}
            self.weights[layerNum][layerNum+1] = Matrix(nextLayer.rows, currentLayer.rows).randomize()
            self.biases[layerNum+1] = Matrix(nextLayer.rows, 1).randomize()
            self.errors[layerNum+1] = Matrix(nextLayer.rows, 1).randomize()

    @staticmethod
    def fromFile(fileName):
        net = None
        with open(fileName, "r") as file:
            lines = file.readlines()
            structure = [int(x) for x in lines[0].split(" ")]
            numLayers = len(structure)
            weights = {}
            biases = {}

            for lineNum in range(1, len(lines)):
                if lineNum % 2 == 1:
                    weights[floor(lineNum/2)] = {}
                    weights[floor(lineNum/2)][floor(lineNum/2)+1] = [float(x) for x in lines[lineNum].split(" ")]
                else:
                    biases[floor(lineNum/2)] = [float(x) for x in lines[lineNum].split(" ")]

            net = PyNet(structure, 0.1)

            for layerNum in range(numLayers - 1):
                currentLayer = net.layers[layerNum]
                nextLayer = net.layers[layerNum + 1]
                net.weights[layerNum] = {}
                net.weights[layerNum][layerNum + 1] = Matrix(nextLayer.rows, currentLayer.rows).load(weights[layerNum][layerNum+1])
                net.biases[layerNum + 1] = Matrix(nextLayer.rows, 1).load(biases[layerNum+1])
                net.errors[layerNum + 1] = Matrix(nextLayer.rows, 1).randomize()

        return net

    def feedForward(self, inputs):
        if len(inputs) != self.layers[0].rows:
            print("Invalid inputs!")
            sys.exit(0)

        inputMatrix = Matrix.fromArray([inputs]).reshape((self.structure[0], 1))

        self.layers[0] = inputMatrix

        for layerNum in range(1, self.numLayers):
            prevLayer = self.layers[layerNum-1]
            prevToCurrWeights = self.weights[layerNum-1][layerNum]
            self.layers[layerNum] = prevToCurrWeights.multiply(prevLayer)
            self.layers[layerNum] = self.layers[layerNum].plus(self.biases[layerNum])
            self.layers[layerNum] = self.layers[layerNum].forEach(Helper.sigmoid)

    def backPropagate(self, targets):
        if len(targets) != self.layers[self.numLayers-1].rows:
            print("Invalid targets!")
            sys.exit(0)

        targetMatrix = Matrix.fromArray([targets]).reshape((self.structure[self.numLayers-1], 1))
        self.errors[self.numLayers-1] = targetMatrix.minus(self.layers[self.numLayers-1])

        temp = self.layers[self.numLayers-1].forEach(Helper.sigmoidPrime)
        temp = self.errors[self.numLayers-1].hadamardProduct(temp)
        temp = temp.times(self.learningRate)

        deltaBiases = temp
        deltaWeights = temp.multiply(self.layers[self.numLayers-2].transpose())
        self.weights[self.numLayers-2][self.numLayers-1] = self.weights[self.numLayers-2][self.numLayers-1].plus(deltaWeights)
        self.biases[self.numLayers-1] = self.biases[self.numLayers-1].plus(deltaBiases)

        for layerNum in range(self.numLayers-2, 0, -1):
            self.errors[layerNum] = self.weights[layerNum][layerNum+1].transpose().multiply(self.errors[layerNum+1])
            temp = self.layers[layerNum].forEach(Helper.sigmoidPrime)
            temp = self.errors[layerNum].hadamardProduct(temp)
            temp = temp.times(self.learningRate)

            deltaBiases = temp
            deltaWeights = temp.multiply(self.layers[layerNum-1].transpose())
            self.weights[layerNum-1][layerNum] = self.weights[layerNum-1][layerNum].plus(deltaWeights)
            self.biases[layerNum] = self.biases[layerNum].plus(deltaBiases)

    def getOutputs(self):
        return self.layers[self.numLayers-1].flatten()

    def test(self):
        while True:
            ip = [int(x) for x in input("Enter inputs : ").split(" ")]
            # op = [int(x) for x in input("Enter targets : ").split(" ")]

            self.feedForward(ip)
            # self.backPropagate(op)
            print("Result : ", self.getOutputs())

    def trainDigit(self, digit, fileName):
        with open(fileName, "r") as file:
            lines = file.readlines()
            for lineNum in range(28):
                print(lines[lineNum])

    def train(self, dataFile, labelFile, epochs = 5):
        dataFile = open(dataFile, "r")
        labelFile = open(labelFile, "r")

        data = dataFile.readlines()
        labels = labelFile.readlines()

        numData = len(data)

        dataList = []

        for i in range(numData):
            item = [data[i], labels[i]]
            dataList.append(item)

        for j in range(epochs):
            shuffle(dataList)
            for i in range(numData):
                d = [float(x) for x in dataList[i][0].split(" ")]
                l = [float(x) for x in dataList[i][1].split(" ")]
                self.feedForward(d)
                self.backPropagate(l)

                err = self.calcError()
                print("Error : ", err)

        dataFile.close()
        labelFile.close()

        self.test()


    def calcError(self):
        err = 0
        for errNum in range(self.errors[self.numLayers-1].rows):
            err += self.errors[self.numLayers-1].array[0][errNum]

        return err/self.errors[self.numLayers-1].rows
