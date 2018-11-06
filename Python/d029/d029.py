def best_match(goals1, goals2):
    if len(goals1) != len(goals2):
        raise Exception("Amount of matches are not equal")
    elif len(goals1) == len(goals2) == 1:
        return 0
    substracts = list()
    for g1, g2 in zip(goals1, goals2):
        substract = g1 - g2
        substracts.append(substract)
    min_value = min(substracts)
    min_value_indexes = [i for i, x in enumerate(substracts) if x == min_value]
    idx, g2_best = 0, 0
    for index in min_value_indexes:
        if goals2[index] > g2_best:
            g2_best = goals2[index]
            idx = index
        elif len(min_value_indexes) == 1:
            idx = index

    return idx


def test():
    assert 1 == best_match([6, 4], [1, 2])
    assert 0 == best_match([1], [0])
    assert 4 == best_match([1, 2, 3, 4, 5], [0, 1, 2, 3, 4])
    assert 2 == best_match([3, 4, 3], [1, 1, 2])
    assert 1 == best_match([4, 3, 4], [1, 1, 1])
    assert 0 == best_match([10, 16, 9, 7, 5, 3, 10, 14, 5, 17, 10, 6, 6, 4], [9, 6, 4, 2, 0, 1, 4, 5, 4, 7, 2, 4, 4, 1])
    assert 3 == best_match([19, 15, 8, 11], [10, 5, 3, 7])
    assert 12 == best_match([14, 10, 9, 14, 6, 16, 5, 13, 13, 10, 16, 6, 6, 14, 19, 9],
                            [10, 7, 3, 5, 3, 10, 4, 10, 8, 0, 9, 4, 5, 6, 10, 3])
    assert 9 == best_match([11, 15, 7, 4, 4, 10, 3, 8, 16, 1],
                           [9, 6, 0, 0, 0, 2, 1, 4, 8, 0])


def main():
    test()


if __name__ == '__main__':
    main()
