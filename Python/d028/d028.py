def find_k(number):
    result = 0
    i = 2
    while i * i <= number:
        while number % i == 0:
            number /= i
            result += 1
        i += 1
    if number > 1:
        result += 1
    return result


def count_Kprimes(k, start, end):
    return [number for number in range(start, end + 1) if find_k(number) == k]


def puzzle(s):
    a = count_Kprimes(1, 0, s)
    b = count_Kprimes(3, 0, s)
    c = count_Kprimes(7, 0, s)

    return sum(i + j + k == s for i in a for j in b for k in c)


def test():
    assert [4, 6, 9, 10, 14, 15, 21, 22, 25, 26, 33, 34, 35, 38, 39, 46, 49, 51, 55, 57, 58, 62, 65, 69, 74, 77, 82, 85,
            86, 87, 91, 93, 94, 95] == count_Kprimes(2, 0, 100)
    assert [8, 12, 18, 20, 27, 28, 30, 42, 44, 45, 50, 52, 63, 66, 68, 70, 75, 76, 78, 92, 98, 99] == count_Kprimes(3, 0, 100)
    assert [1020, 1026, 1032, 1044, 1050, 1053, 1064, 1072, 1092, 1100] == count_Kprimes(5, 1000, 1100)
    assert [500, 520, 552, 567, 588, 592, 594] == count_Kprimes(5, 500, 600)


def main():
    test()


if __name__ == '__main__':
    main()
