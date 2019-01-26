import sys
sys.path.append('../../')
from Net import PyNet

structure = [2, 3, 3, 2, 1]

net = PyNet(structure, 0.1)

net.train("data.txt", "labels.txt")

net.layers[0].print()
