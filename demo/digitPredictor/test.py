import sys
from random import randint
import os

sys.path.append("../../")

from PyNet import PyNet


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
    net = PyNet.fromFile("trained.net")

    while True:
        x = input("Enter a test num : ")
        test(net, x)


if __name__ == "__main__":
    main()
