def count(string: str):
    unique_chars = set(string)
    return {char: string.count(char) for char in unique_chars}


def test():
    assert count('aba') == {'a': 2, 'b': 1}
    assert count('') == {}


def main():
    test()


if __name__ == '__main__':
    main()
