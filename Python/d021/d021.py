def domain_name(url):
    domain = url.split("//")[-1].split("/")[0]
    splitter = domain.split(".")
    domain = splitter[0] if len(splitter) == 2 else splitter[1]
    return domain


def test():
    assert domain_name("http://github.com/carbonfive/raygun") == "github"
    assert domain_name("http://www.zombie-bites.com") == "zombie-bites"
    assert domain_name("https://www.cnet.com") == "cnet"
    assert domain_name("www.xakep.ru") == "xakep"


def main():
    test()


if __name__ == '__main__':
    main()
