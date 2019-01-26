from Net import PyNet


def main():
    structure = [2, 3, 2]
    net = PyNet(structure)
    net.getLayer(0).print()
    net.getLayer(0).setData([0, 1])
    net.getLayer(0).print()

if __name__ == "__main__":
    main()
