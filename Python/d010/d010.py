import re


def increment_string(strng):
    regex = re.compile(r'(\d+)').findall(strng)

    if not regex and not strng:
        return "1"

    if not regex and strng:
        position = (len(strng) + 1)
        new_number = "1"
    else:
        position = strng.find(regex[-1])
        new_number = format(int(regex[-1]) + 1, "0" + str(len(regex[-1])) + "d")

    strng = strng[:position] + new_number

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
    assert increment_string("\g('j592271429B9751100000269") == "\g('j592271429B9751100000270"
    assert increment_string("802<2070577785511V_F!5D8biJMt77}[Hx28778297,e#oJ520828210[37~9O[ 000000000800") == \
           "802<2070577785511V_F!5D8biJMt77}[Hx28778297,e#oJ520828210[37~9O[ 000000000801"


def main():
    test()


if __name__ == '__main__':
    main()
