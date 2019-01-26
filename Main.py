from Net import PyNet


def main():
    structure = [2, 3, 2]
    net = PyNet(structure)
    print(net.getOutput())
    net.feedForward([0, 1])
    print(net.getOutput())
    net.backPropagate([0, 1])
    net.feedForward([0, 1])
    print(net.getOutput())

if __name__ == "__main__":
    main()
