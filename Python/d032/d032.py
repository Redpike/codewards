import functools


@functools.lru_cache(None)
def rec_function(n: int):
    if n < 2:
        return 1
    else:
        return rec_function(n - 1) + n


def get_colour(number: int):
    return 'red' if number % 3 == 1 else 'yellow' if number % 3 == 2 else 'blue'


def same_col_seq(val, k, col):
    values = []
    for i in range(1, 1_500):
        value = rec_function(i)
        if value > val:
            colour = get_colour(value)
            if colour is col and len(values) <= k:
                values.append(value)
                if len(values) == k:
                    break
    return values


def test():
    assert [6, 15, 21] == same_col_seq(3, 3, 'blue')
    assert [136, 190, 253, 325] == same_col_seq(100, 4, 'red')
    assert [] == same_col_seq(250, 6, 'yellow')
    assert [1081, 1225, 1378, 1540, 1711, 1891, 2080] == same_col_seq(1000, 7, 'red')


def main():
    test()


if __name__ == '__main__':
    main()
