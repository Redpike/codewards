import re

import numpy as np


def get_number_of_even_digits(number):
    pattern = r'[24680]'
    return len(re.findall(pattern, str(number)))


def get_primes(n):
    assert n >= 2
    sieve = np.ones(n // 2, dtype=np.bool)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = False
    return np.r_[2, 2 * np.nonzero(sieve)[0][1::] + 1]


def primes(n):
    primes = sorted(get_primes(n), reverse=True)
    max_number, max_even_digits = 0, 0
    for number in primes:
        even_digits = get_number_of_even_digits(number)
        if even_digits > max_even_digits:
            max_even_digits = even_digits
            max_number = number
    return max_number


def f(n):
    return primes(n)


def test():
    assert 887 == f(1000)
    assert 1201 == f(1210)
    assert 8887 == f(10000)
    assert 487 == f(500)
    assert 467 == f(487)


def main():
    test()


if __name__ == '__main__':
    main()
