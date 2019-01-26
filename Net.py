from Layer import Layer


class PyNet:
    def __init__(self, structure):
        self.structure = structure
        self.numLayers = len(structure)
        self.layers = []
        for layerNum in range(self.numLayers):
            numNeuronsNext = 0
            if layerNum != self.numLayers - 1:
                numNeuronsNext = structure[layerNum + 1]
            layer = Layer(structure[layerNum], numNeuronsNext, layerNum, self)
            self.layers.append(layer)

    def getLayer(self, layerNum):
        if layerNum >= self.numLayers - 1:
            return None
        return self.layers[layerNum]

    def feedForward(self, inputData):
        inputLayer = self.layers[0]

        self.print("Before")

        inputLayer.setData(inputData)

        for layer in self.layers:
            layer.feedForward()

        self.print("After")


    def print(self, msg = ""):
        print(msg)
        for layer in self.layers:
            layer.print()
