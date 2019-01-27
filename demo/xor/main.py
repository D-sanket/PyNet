import sys
sys.path.append('../../')
from PyNet import PyNet

structure = [2, 2, 1]

net = PyNet(structure, 0.1)

net.train("data.txt", "labels.txt")

