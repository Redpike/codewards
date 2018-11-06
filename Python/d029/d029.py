def best_match(goals1, goals2):
    # coding and coding..


def test():
    assert 1 == best_match([6, 4], [1, 2])
    assert 0 == best_match([1], [0])
    assert 4 == best_match([1, 2, 3, 4, 5], [0, 1, 2, 3, 4])
    assert 2 == best_match([3, 4, 3], [1, 1, 2])
    assert 1 == best_match([4, 3, 4], [1, 1, 1])


def main():
    test()


if __name__ == '__main__':
    main()