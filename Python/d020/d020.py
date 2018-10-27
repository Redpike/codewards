def chained(functions):
    def apply(param):
        result = param
        for func in functions:
            result = func(result)
        return result
    return apply


def test():
    def f1(x):
        return x * 2

    def f2(x):
        return x + 2

    def f3(x):
        return x ** 2

    def f4(x):
        return x.split()

    def f5(xs):
        return [x[::-1].title() for x in xs]

    def f6(xs):
        return "_".join(xs)

    assert chained([f1, f2, f3])(0) == 4
    assert chained([f1, f2, f3])(2) == 36
    assert chained([f3, f2, f1])(2) == 12
    assert chained([f4, f5, f6])("lorem ipsum dolor") == "Merol_Muspi_Rolod"


def main():
    test()


if __name__ == '__main__':
    main()
