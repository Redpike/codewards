def separate_by_comma(names, last_index):
    likes_string = ''
    for index in range(0, last_index):
        likes_string += str(names[index]) + ', '
    return likes_string[:-2]


def likes(names):
    if not names:
        return 'no one likes this'
    elif len(names) == 1:
        return names[0] + ' likes this'
    elif 1 < len(names) < 4:
        last_index = len(names) - 1
        likes_string = separate_by_comma(names, last_index)
        likes_string += ' and ' + str(names[-1]) + ' like this'
        return likes_string
    else:
        likes_string = separate_by_comma(names, 2)
        likes_string += ' and ' + str(len(names) - 2) + ' others like this'
        return likes_string


def test():
    assert likes([]) == 'no one likes this'
    assert likes(['Peter']) == 'Peter likes this'
    assert likes(['Jacob', 'Alex']) == 'Jacob and Alex like this'
    assert likes(['Max', 'John', 'Mark']) == 'Max, John and Mark like this'
    assert likes(['Alex', 'Jacob', 'Mark', 'Max']) == 'Alex, Jacob and 2 others like this'


def main():
    test()


if __name__ == '__main__':
    main()
