def wave(string):
    results = []
    for index, char in enumerate(string):
        upper_char = string[index].upper()

        if str(char).isspace():
            continue

        mexican_string = string[:index] + upper_char + string[index + 1:]
        results.append(mexican_string)

    return results


def test():
    assert wave("hello") == ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
    assert wave("codewars") == ["Codewars", "cOdewars", "coDewars", "codEwars", "codeWars", "codewArs", "codewaRs", "codewarS"]
    assert wave("two words") == ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"]
    assert wave(" gap ") == [" Gap ", " gAp ", " gaP "]


def main():
    test()


if __name__ == '__main__':
    main()
