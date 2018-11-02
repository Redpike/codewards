class Plugboard(object):
    pairs = []

    def __init__(self, wires=None):
        """
        wires: This is the mapping of pairs of characters
        """
        if wires is None:
            wires = ""
        if len(set(wires)) != len(wires):
            raise Exception("Should not have accepted a second definition for a wire end")
        if len(wires) / 2 > 10:
            raise Exception("Should not have accepted too many wires defined")
        self.pairs = [[wires[index], wires[index + 1]] for index in range(0, len(wires), 2)]
        pass

    def process(self, c):
        """
        c: The single character to process
        """
        for pair in self.pairs:
            if c in pair:
                return pair[0] if pair.index(c) == 1 else pair[1]
        return c


def test():
    plugboard = Plugboard("AB")
    assert "B" == plugboard.process("A")
    assert "A" == plugboard.process("B")
    assert "C" == plugboard.process("C")


def main():
    test()


if __name__ == '__main__':
    main()
