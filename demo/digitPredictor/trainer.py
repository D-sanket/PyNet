import sys
from random import randint
import os

sys.path.append("../../")

from PyNet import PyNet


def saveToFile(net):
    with open("trained.net", "w") as file:
        structure = " ".join([str(x) for x in net.structure])
        numLayers = net.numLayers
        file.write(structure + "\n")
        for layerNum in range(numLayers - 1):
            weights = net.weights[layerNum][layerNum + 1]
            weights = weights.flatten()
            weights = " ".join([str(x) for x in weights])
            file.write(weights + "\n")

            biases = " ".join([str(x) for x in net.biases[layerNum+1].flatten()])

            file.write(biases+"\n")


def test(net, n):
    path1 = "/home/CiPHER/PycharmProjects/PyNet/demo/digitPredictor/data/" + str(n) + "/1." + str(n)
    with open(path1, "r") as file1:
        lines1 = file1.readlines()
        inputs1 = []
        for lineNum1 in range(28):
            line1 = lines1[lineNum1]
            arr1 = [int(x) for x in line1[:-1]]
            inputs1 += arr1
        net.feedForward(inputs1)
        output = net.getOutputs()
        maxI = 0
        maxNum = output[0]

        for oIdx in range(10):
            if output[oIdx] > maxNum:
                maxNum = output[oIdx]
                maxI = oIdx

        print("Guess : ", str(maxI))


def main():
    nums = {}

    maxIterations = 10000
    iterationCount = 0

    # net = PyNet([784, 28, 28, 10], 0.1)

    net = PyNet.fromFile("trained.net")

    for i in range(10):
        path = "/home/CiPHER/PycharmProjects/PyNet/demo/digitPredictor/data/" + str(i)
        files = os.listdir(path)
        nums[i] = len(files)

    while iterationCount < maxIterations:
        try:
            num = randint(0, 9)
            targets = []
            for i in range(10):
                if i == num:
                    targets.append(1)
                else:
                    targets.append(0)
            maxN = nums[num]
            fileName = "/home/CiPHER/PycharmProjects/PyNet/demo/digitPredictor/data/" + str(num) + "/" + str(
                randint(1, maxN)) + "." + str(num)
            with open(fileName, "r") as file:
                lines = file.readlines()
                inputs = []
                for lineNum in range(28):
                    line = lines[lineNum]
                    arr = [float(x) for x in line[:-1]]
                    inputs += arr
                net.feedForward(inputs)
                net.backPropagate(targets)
            iterationCount += 1

            output = net.getOutputs()
            maxI = 0
            maxNum = output[0]

            for oIdx in range(10):
                if output[oIdx] > maxNum:
                    maxNum = output[oIdx]
                    maxI = oIdx
            print("i : ", iterationCount, "\tn : ", num, "\tg : ", maxI)
            # print(net.weights[1][2].array[0][0])
        except Exception as ex:
            pass

    saveToFile(net)

    while True:
        x = input("Enter a test num : ")
        test(net, x)


if __name__ == "__main__":
    main()
