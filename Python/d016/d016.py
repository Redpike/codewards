def make_password(phrase):
    words_in_phrase = phrase.split()
    first_letters = [word[0] for word in words_in_phrase]
    for index, char in enumerate(first_letters):
        if char.lower() == "i":
            first_letters[index] = str(1)
        elif char.lower() == "o":
            first_letters[index] = str(0)
        elif char.lower() == "s":
            first_letters[index] = str(5)
    return ''.join(first_letters)


def test():
    assert make_password("Give me liberty or give me death") == "Gml0gmd"
    assert make_password("Keep Calm and Carry On") == "KCaC0"


def main():
    test()


if __name__ == '__main__':
    main()