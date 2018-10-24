def rot(strng):
    lines = strng.split("\n")
    result = []
    for line in lines:
        result.append(line[::-1])
    result.reverse()
    return "\n".join(result)


def selfie_and_rot(strng):
    lines = strng.split("\n")
    doted_result = []
    roted_result = []
    for line in lines:
        dots = len(line) * "."
        doted_result.append(line + dots)
        roted_result.append(dots + line[::-1])
    roted_result.reverse()
    result_string = "\n".join(doted_result) + "\n" + "\n".join(roted_result)
    print(result_string)
    return result_string


def oper(fct, s):
    return fct(s)


def test():
    assert oper(rot, "fijuoo\nCqYVct\nDrPmMJ\nerfpBA\nkWjFUG\nCVUfyL") \
           == "LyfUVC\nGUFjWk\nABpfre\nJMmPrD\ntcVYqC\nooujif"
    assert oper(rot, "rkKv\ncofM\nzXkh\nflCB") == "BClf\nhkXz\nMfoc\nvKkr"
    assert oper(selfie_and_rot, "xZBV\njsbS\nJcpN\nfVnP") == \
           "xZBV....\njsbS....\nJcpN....\nfVnP....\n....PnVf\n....NpcJ\n....Sbsj\n....VBZx"
    assert oper(selfie_and_rot, "uLcq\nJkuL\nYirX\nnwMB") == \
           "uLcq....\nJkuL....\nYirX....\nnwMB....\n....BMwn\n....XriY\n....LukJ\n....qcLu"


def main():
    test()


if __name__ == '__main__':
    main()
