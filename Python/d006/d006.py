def reverse_or_rotate(string, limit):
    sum_of_cubes = 0
    for index, digit in enumerate(string):
        sum_of_cubes += pow(int(digit), 3)

    if sum_of_cubes % 2 == 0:
        return string[::-1]

    return string[1:limit] + string[0]


def revrot(string, sz):
    if sz <= 0 or not string or sz > len(string):
        return ""

    result = ""
    list_of_strings = map(''.join, zip(*[iter(string)] * sz))

    for strng in list_of_strings:
        result += reverse_or_rotate(''.join(strng), sz)

    return result


def test():
    assert revrot("1234", 0) == ""
    assert revrot("", 0) == ""
    assert revrot("1234", 5) == ""
    assert revrot("733049910872815764", 5) == "330479108928157"


def main():
    test()


if __name__ == '__main__':
    main()
