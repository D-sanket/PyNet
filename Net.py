from Layer import Layer


class PyNet:
    def __init__(self, structure, learningRate = 0.1):
        self.structure = structure
        self.learningRate = learningRate
        self.numLayers = len(structure)
        self.layers = []
        for layerNum in range(self.numLayers):
            numNeuronsNext = 0
            if layerNum != self.numLayers - 1:
                numNeuronsNext = structure[layerNum + 1]
            layer = Layer(structure[layerNum], numNeuronsNext, layerNum, self)
            self.layers.append(layer)

    def getLayer(self, layerNum):
        if layerNum > self.numLayers - 1:
            return None
        return self.layers[layerNum]

    def feedForward(self, inputData):
        inputLayer = self.layers[0]

        inputLayer.setData(inputData)
        inputLayer.feedForward()

        for layerNum in range(self.numLayers):
            if layerNum == 0:
                continue
            layer = self.layers[layerNum]
            layer.feedForward()

    def backPropagate(self, targetData):
        outputLayer = self.layers[self.numLayers-1]
        errors = [[], []]

        for neuronNum in range(outputLayer.length):
            neuron = outputLayer.getNeuron(neuronNum)
            neuron.deactivate()
            error = targetData[neuronNum] - neuron.getData()
            errors[0].append(error)
            b = neuron.getBias()
            newBias = b - errors[0][neuronNum]*self.learningRate
            neuron.setBias(newBias)

        for layerNum in range(self.numLayers-2, -1, -1):
            errors[1] = []
            layer = self.layers[layerNum]
            nxtLayer = layer.nextLayer()

            for neuronNum in range(layer.length):
                neuron = layer.getNeuron(neuronNum)
                newBias = 0
                neuron.setBias(newBias)

            for neuronNum in range(layer.length):
                error = 0
                neuron = layer.getNeuron(neuronNum)
                neuron.deactivate()
                for nxtNeuronNum in range(nxtLayer.length):
                    nxtNeuron = nxtLayer.getNeuron(nxtNeuronNum)
                    weight = neuron.getWeight(nxtNeuronNum)
                    error += weight * errors[0][nxtNeuronNum]
                errors[1].append(error)

                for nxtNeuronNum in range(nxtLayer.length):
                    nxtNeuron = nxtLayer.getNeuron(nxtNeuronNum)
                    weight = neuron.getWeight(nxtNeuronNum)
                    newWeight = weight - self.learningRate*weight*errors[0][nxtNeuronNum]
                    neuron.setWeight(nxtNeuronNum, newWeight)

                newBias = neuron.getBias() + errors[1][neuronNum] * self.learningRate
                neuron.setBias(newBias)

            for neuronNum in range(layer.length):
                neuron = layer.getNeuron(neuronNum)
                newBias = neuron.getBias()/layer.length
                neuron.setBias(newBias)

            errors[0] = errors[1]

    def getOutput(self):
        outputLayer = self.layers[self.numLayers-1]
        result = []

        for neuron in outputLayer.getNeurons():
            result += [neuron.getData()]
        return result

    def print(self, msg = ""):
        print(msg)
        for layer in self.layers:
            layer.print()

    def train(self, dataFileName, labelFileName):
        data = open(dataFileName, "r")
        labels = open(labelFileName, "r")

        dataArray = data.readlines()
        labelsArray = labels.readlines()

        numData = len(dataArray)

        for i in range(numData):
            x, y = [int(d) for d in dataArray[i].split(" ")]
            z = int(labelsArray[i])

            self.feedForward([x, y])
            self.backPropagate([z])

            print(self.getOutput(), [x, y])

        data.close()
        labels.close()
