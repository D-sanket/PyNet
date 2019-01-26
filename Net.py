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

        for layer in self.layers:
            layer.feedForward()

    def backPropagate(self, targetData):
        outputLayer = self.layers[self.numLayers-1]
        errors = [[], []]

        for neuronNum in range(outputLayer.length):
            neuron = outputLayer.getNeuron(neuronNum)
            neuron.deactivate()
            error = targetData[neuronNum] - neuron.getData()
            errors[0].append(error)

        for layerNum in range(self.numLayers-2, -1, -1):
            errors[1] = []
            layer = self.layers[layerNum]
            nxtLayer = layer.nextLayer()

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

                b = neuron.getBias()
                newBias = b - errors[0][nxtNeuronNum] * self.learningRate
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
