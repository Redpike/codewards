import re


def printer_error(string):
    chars_counter = 0
    found_list = re.compile(r'[^a-m]+').findall(string)
    for x in found_list:
        chars_counter += len(x)
    result = [str(chars_counter), '/', str(len(string))]
    return ''.join(result)


def test():
    string = 'aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz'
    assert printer_error(string) == '3/56'


def main():
    test()


if __name__ == '__main__':
    main()
