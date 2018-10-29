def longest_consec(strarr, k):
    if not strarr or k > len(strarr) or k <= 0:
        return ""
    result = ""
    for index in range(len(strarr) - k + 1):
        s = "".join(strarr[index:index + k])
        if len(s) > len(result):
            result = s

    return result


def test():
    assert longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2) == "abigailtheta"
    assert longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"],
                          1) == "oocccffuucccjjjkkkjyyyeehh"
    assert longest_consec([], 3) == ""
    assert longest_consec(["itvayloxrp", "wkppqsztdkmvcuwvereiupccauycnjutlv", "vweqilsfytihvrzlaodfixoyxvyuyvgpck"],
                          2) == "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck"
    assert longest_consec(["wlwsasphmxx", "owiaxujylentrklctozmymu", "wpgozvxxiu"],
                          2) == "wlwsasphmxxowiaxujylentrklctozmymu"
    assert longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2) == ""
    assert longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 3) == "ixoyx3452zzzzzzzzzzzz"
    assert longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 15) == ""
    assert longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 0) == ""


def main():
    test()


if __name__ == '__main__':
    main()
