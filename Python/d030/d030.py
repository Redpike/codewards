def are_negatives(arr):
    return len([num for num in arr if num < 0]) == len(arr)


def kadane_algorithm(arr):
    best = [-1] * len(arr)
    best[0] = arr[0]
    for i in range(1, len(arr)):
        best[i] = max(arr[i], best[i - 1] + arr[i])
    return max(best)


def maxSequence(arr):
    if not arr or are_negatives(arr):
        return 0
    return kadane_algorithm(arr)


def test():
    assert 0 == maxSequence([])
    assert 0 == maxSequence([-1, -2, -3])
    assert 6 == maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])


def main():
    test()


if __name__ == '__main__':
    main()
