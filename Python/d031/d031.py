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
        return "zero"
    number_str = str(n)
    number_len = len(number_str)
    groups = (number_len + 2) // 3
    number_str = number_str.zfill(groups * 3)
    for i in range(0, groups * 3, 3):
        hundreds, tns, unts, = int(number_str[i]), int(number_str[i + 1]), int(number_str[i + 2])
        group = groups - (i / 3 + 1)
        if hundreds >= 1:
            words.append(units[hundreds])
            if tns > 0:
                words.append(" hundred ")
            else:
                words.append(" hundred")
        if tns > 1:
            words.append(tens[tns])
            if unts >= 1:
                words.append("-" + units[unts])
        elif tns == 1:
            if unts >= 1:
                words.append(teens[unts])
            else:
                words.append(tens[tns])
        else:
            if unts >= 1:
                if hundreds > 0:
                    words.append(" " + units[unts])
                else:
                    words.append(units[unts])
        if group >= 1 and (hundreds + tns + unts) > 0:
            if tns > 0 or unts > 0 or groups > 1:
                words.append(" " + thousands[int(group)] + " ")
            else:
                words.append(" " + thousands[int(group)])
    return "".join(words).strip()


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
