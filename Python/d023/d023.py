def tickets(people):
    cashier = {
        100: 0,
        50: 0,
        25: 0
    }
    for payment in people:
        if payment == 25:
            cashier[25] += 1
        elif payment == 50:
            if cashier[25] < 1:
                return "NO"
            cashier[50] += 1
            cashier[25] -= 1
        elif payment == 100:
            cashier[100] += 1
            if cashier[25] >= 1 and cashier[50] >= 1:
                cashier[50] -= 1
                cashier[25] -= 1
            elif cashier[25] >= 3:
                cashier[25] -= 3
            else:
                return "NO"
        else:
            return "NO"
    return "YES"


def test():
    assert tickets([25, 25, 50]) == "YES"
    assert tickets([25, 100]) == "NO"


def main():
    test()


if __name__ == '__main__':
    main()
