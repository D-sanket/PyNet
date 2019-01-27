import sys
sys.path.append('../../')
from PyNet import PyNet

structure = [1, 1]

net = PyNet(structure, 0.5)

net.train("data.txt", "labels.txt")

