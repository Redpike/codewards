def dashatize(num):
    try:
        positive_integer = str(abs(int(num)))
    except TypeError:
        return "None"

    digits_in_num = "-".join(positive_integer)
    copy_of_digits = digits_in_num[::]
    occurrences = 0

    for index, char in enumerate(digits_in_num):
        if char is "-":
            if int(digits_in_num[index - 1]) % 2 == 0 and int(digits_in_num[index + 1]) % 2 == 0:
                copy_of_digits = copy_of_digits[:index - occurrences] + copy_of_digits[index + 1 - occurrences:]
                occurrences += 1
    return copy_of_digits


def test():
    assert dashatize(274) == "2-7-4"
    assert dashatize(5311) == "5-3-1-1"
    assert dashatize(86320) == "86-3-20"
    assert dashatize(974302) == "9-7-4-3-02"
    assert dashatize(None) == "None"
    assert dashatize(0) == "0"
    assert dashatize(-1) == "1"
    assert dashatize(-28369) == "28-3-6-9"


def main():
    test()


if __name__ == '__main__':
    main()
