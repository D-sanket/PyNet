from Net import PyNet


def main():
    structure = [2, 3, 2]
    net = PyNet(structure)
    net.feedForward([0, 1])

if __name__ == "__main__":
    main()
