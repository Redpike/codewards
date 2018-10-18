def Descending_Order(num):
    list_of_digits = list(str(num))
    return int(''.join(sorted(list_of_digits, reverse=True)))


def test():
    assert Descending_Order(0) == 0
    assert Descending_Order(15) == 51
    assert Descending_Order(123456789) == 987654321


def main():
    test()


if __name__ == '__main__':
    main()
