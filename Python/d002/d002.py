def reverse_words(text):
    list_of_words = text.split(" ")
    list_of_reversed_words = list()
    for string in list_of_words:
        list_of_reversed_words.append(string[::-1])
    text = " ".join(list_of_reversed_words)
    return text


def test():
    assert reverse_words('The quick brown fox jumps over the lazy dog.') == 'ehT kciuq nworb xof spmuj revo eht yzal .god'
    assert reverse_words('apple') == 'elppa'
    assert reverse_words('a b c d') == 'a b c d'
    assert reverse_words('double  spaced  words') == 'elbuod  decaps  sdrow'


def main():
    test()


if __name__ == '__main__':
    main()
