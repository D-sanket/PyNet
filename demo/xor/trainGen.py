import sys
from random import randint

dataCount = 1000

if len(sys.argv) > 1:
    dataCount = int(sys.argv[1])
data = open("data.txt", "w")
labels = open("labels.txt", "w")
for i in range(dataCount):
    x = randint(0, 1)
    y = randint(0, 1)
    z = 1
    if x == y:
        z = 0

    labels.write(str(z)+"\n")
    data.write(str(x)+" "+str(y)+"\n")

data.close()
labels.close()
