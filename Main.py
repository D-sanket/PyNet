from PyNet import PyNet


def main():
    structure = [2, 3, 2]
    net = PyNet(structure)
    net.feedForward([1, 1])
    print(net.weights[0][1].toArray())
    net.backPropagate([1, 1])
    print(net.weights[0][1].toArray())

if __name__ == "__main__":
    main()
