import re


def increment_string(strng):
    regex = re.compile(r'(\d+)').findall(strng)

    if not regex and not strng:
        return "1"

    if not regex and strng:
            new_number = "1"
    else:
        new_number = format(int(regex[0]) + 1, "0" + str(len(regex[0])) + "d")

    regex = re.compile(r'[A-Za-z]+').findall(strng)

    if regex:
        strng = regex[0] + new_number
    else:
        strng = new_number

    return strng


def test():
    assert increment_string("foo") == "foo1"
    assert increment_string("foobar001") == "foobar002"
    assert increment_string("foobar1") == "foobar2"
    assert increment_string("foobar00") == "foobar01"
    assert increment_string("foobar99") == "foobar100"
    assert increment_string("foobar099") == "foobar100"
    assert increment_string("") == "1"
    assert increment_string("1") == "2"
    assert increment_string("009") == "010"


def main():
    test()


if __name__ == '__main__':
    main()
