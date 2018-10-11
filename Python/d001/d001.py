def high_and_low(numbers):
    list_of_numbers = list(map(int, (numbers.split(" "))))
    max_element = max(list_of_numbers)
    min_element = min(list_of_numbers)
    numbers = str(max_element) + " " + str(min_element)
    return numbers


def test():
    assert high_and_low("1 2 3 4 5") == "5 1"
    assert high_and_low("1 2 -3 4 5") == "5 -3"
    assert high_and_low("1 9 3 4 -5") == "9 -5"
    assert high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6") == "542 -214"


def main():
    test()


if __name__ == '__main__':
    main()
