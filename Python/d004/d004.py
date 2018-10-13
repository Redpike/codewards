def expanded_form(num):
    results = []
    for i, digit in enumerate(str(num)[::-1]):
        if int(digit) != 0:
            results.append(digit + ('0' * i))
    return ' + '.join(results[::-1])


def test():
    assert expanded_form(12) == '10 + 2'
    assert expanded_form(42) == '40 + 2'
    assert expanded_form(70304) == '70000 + 300 + 4'


def main():
    test()


if __name__ == '__main__':
    main()
