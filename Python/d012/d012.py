def toJadenCase(string):
    return ' '.join([strng.capitalize() for strng in string.split()])


def test():
    assert toJadenCase("How can mirrors be real if our eyes aren't real") \
           == "How Can Mirrors Be Real If Our Eyes Aren't Real"


def main():
    test()


if __name__ == '__main__':
    main()
