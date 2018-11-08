units = [
    "",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

teens = [
    "",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen"
]

tens = [
    "",
    "ten",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety"
]

thousands = [
    "",
    "thousand",
    "million"
]


def number2words(n):
    words = []
    if n == 0:
        words.append("zero")

    return " ".join(words[])


def test():
    assert "zero" == number2words(0)
    assert "one" == number2words(1)
    assert "eight" == number2words(8)
    assert "ten" == number2words(10)
    assert "nineteen" == number2words(19)
    assert "twenty" == number2words(20)
    assert "twenty-two" == number2words(22)
    assert "fifty-four" == number2words(54)
    assert "eighty" == number2words(80)
    assert "ninety-eight" == number2words(98)
    assert "one hundred" == number2words(100)
    assert "three hundred one" == number2words(301)
    assert "seven hundred ninety-three" == number2words(793)
    assert "eight hundred" == number2words(800)
    assert "six hundred fifty" == number2words(650)
    assert "one thousand" == number2words(1000)
    assert "one thousand three" == number2words(1003)


def main():
    test()


if __name__ == '__main__':
    main()
