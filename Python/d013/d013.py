import re


def abbreviate(s):
    list_of_words = re.findall(r'[A-Za-z]{4,}', s)

    for word in list_of_words:
        a10n_word = word[0] + str(len(word) - 2) + word[-1]
        s = s.replace(word, a10n_word)

    return s


def test():
    assert abbreviate("internationalization") == "i18n"
    assert abbreviate("accessibility") == "a11y"
    assert abbreviate("Accessibility") == "A11y"
    assert abbreviate("elephant-ride") == "e6t-r2e"
    assert abbreviate("sat_the-double-barreled, double-barreled: ") == "sat_the-d4e-b6d, d4e-b6d: "


def main():
    test()


if __name__ == '__main__':
    main()
