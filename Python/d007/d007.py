def find_it(array):
    numbers = {}
    for i in array:
        if i in numbers.keys():
            numbers[i] += 1
        else:
            numbers[i] = 1
    for key, value in numbers.items():
        if value % 2 != 0:
            return int(key)


def test():
    assert find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]) == 5


def main():
    test()


if __name__ == '__main__':
    main()
