def gap(g, m, n):
    if g < 2 or m <= 2 or n <= m:
        return None

    previous_prime = None
    for possible_prime in range(m, n + 1):
        if all(possible_prime % number != 0 for number in range(2, int(possible_prime ** 0.5) + 1)):
            if previous_prime is not None and possible_prime - previous_prime == g:
                return [previous_prime, possible_prime]
            previous_prime = possible_prime
    return None


def test():
    assert gap(2, 100, 110) == [101, 103]
    assert gap(4, 100, 110) == [103, 107]
    assert gap(6, 100, 110) is None
    assert gap(8, 300, 400) == [359, 367]
    assert gap(10, 300, 400) == [337, 347]


def main():
    test()


if __name__ == '__main__':
    main()
