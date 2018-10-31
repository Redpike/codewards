def highest_rank(arr):
    dictionary = {number: arr.count(number) for number in arr}
    list_of_max = [key for key, value in dictionary.items() if value == max(dictionary.values())]
    return max(list_of_max)


def test():
    assert 12 == highest_rank([10, 12, 8, 12, 10, 6, 4, 10, 12])
    assert 10 == highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 10])


def main():
    test()


if __name__ == '__main__':
    main()
