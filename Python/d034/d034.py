import functools


@functools.lru_cache(None)
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)


@functools.lru_cache(None)
def pad(n):
    if n == 0:
        return 1
    elif n == 1 or n == 2:
        return 0
    else:
        return pad(n - 3) + pad(n - 2)


@functools.lru_cache(None)
def jac(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return jac(n - 1) + (2 * jac(n - 2))


@functools.lru_cache(None)
def pel(n):
    if n < 2:
        return n
    else:
        return 2 * pel(n - 1) + pel(n - 2)


@functools.lru_cache(None)
def tri(n):
    if n < 2:
        return 0
    elif n == 2:
        return 1
    else:
        return tri(n - 1) + tri(n - 2) + tri(n - 3)


@functools.lru_cache(None)
def tet(n):
    if n < 3:
        return 0
    elif n == 3:
        return 1
    else:
        return tet(n - 1) + tet(n - 2) + tet(n - 3) + tet(n - 4)


def mixbonacci(pattern, length):
    result = []
    if len(pattern) == 0 or length == 0:
        return result
    if length > len(pattern):
        pattern *= round((length / len(pattern)) + 1)
    counter = {}
    for seq in pattern:
        counter[seq] = 0
    for i in range(0, len(pattern)):
        result.append(eval(pattern[i] + '(' + str(counter[pattern[i]]) + ')'))
        counter[pattern[i]] += 1
    return result[:length]


def test():
    assert [] == mixbonacci([], 10)
    assert [] == mixbonacci(['fib'], 0)
    assert [0, 1, 1, 2, 3, 5, 8, 13, 21, 34] == mixbonacci(['fib'], 10)
    assert [1, 0, 0, 1, 0, 1, 1, 1, 2, 2] == mixbonacci(['pad'], 10)
    assert [0, 1, 1, 3, 5, 11, 21, 43, 85, 171] == mixbonacci(['jac'], 10)
    assert [0, 1, 2, 5, 12, 29, 70, 169, 408, 985] == mixbonacci(['pel'], 10)
    assert [0, 0, 1, 1, 2, 4, 7, 13, 24, 44] == mixbonacci(['tri'], 10)
    assert [0, 0, 0, 1, 1, 2, 4, 8, 15, 29] == mixbonacci(['tet'], 10)
    assert [0, 0, 1, 0, 1, 0, 2, 1, 3, 1] == mixbonacci(['fib', 'tet'], 10)
    assert [0, 1, 0, 1, 3, 1, 5, 11, 2, 21] == mixbonacci(['jac', 'jac', 'pel'], 10)


def main():
    test()


if __name__ == '__main__':
    main()
