import operator
import functools


def persistence(n):
    counter = 0
    list_of_digits = [int(x) for x in str(n)]
    while len(list_of_digits) > 1:
        result = functools.reduce(operator.mul, list_of_digits, 1)
        list_of_digits.clear()
        list_of_digits = [int(x) for x in str(result)]
        counter += 1
    return counter


def test():
    assert persistence(39) == 3
    assert persistence(4) == 0
    assert persistence(25) == 2
    assert persistence(999) == 4


def main():
    test()


if __name__ == '__main__':
    main()
