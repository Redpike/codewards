import string


def title_case(title: str, minor_words=''):
    need_to_not_capitalize = [minor.lower() for minor in minor_words.split()
                              if minor.lower() in title.lower() and minor.lower() is not title.split()[0].lower()]
    title = string.capwords(title)
    words_in_title = title.split()
    for index, word in enumerate(words_in_title):
        if index > 0 and word.lower() in need_to_not_capitalize:
            words_in_title[index] = word.lower()
    return ' '.join(words_in_title)


def test():
    assert title_case('') == ''
    assert title_case('a clash of KINGS', 'a an the of') == 'A Clash of Kings'
    assert title_case('THE WIND IN THE WILLOWS', 'The In') == 'The Wind in the Willows'
    assert title_case('the quick brown fox') == 'The Quick Brown Fox'


def main():
    test()


if __name__ == '__main__':
    main()
