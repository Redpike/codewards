def sort_array(source_array):
    sorted_odd_array = sorted([item for item in source_array if item % 2 != 0])
    odd_index = 0
    for index in range(len(source_array)):
        if source_array[index] % 2 != 0:
            source_array[index] = sorted_odd_array[odd_index]
            odd_index += 1
    return source_array


def test():
    assert sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
    assert sort_array([5, 3, 1, 8, 0]) == [1, 3, 5, 8, 0]
    assert sort_array([]) == []


def main():
    pass


if __name__ == '__main__':
    main()
