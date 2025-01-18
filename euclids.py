def gcd(m, n):
    '''
    Finds the Greatest common denominator of 2 values
    args:
    m: non-zero int
    n: non-zero int
    Examples:
        >>> gcd(12, 24)
        12
        >>> gcd(60, 24)
        12
        >>> gcd(18, 100)
        2
    '''
    if n == 0:
        return m
    return gcd(n, m%n)


def main():
    first_int = int(input("Give first number"))
    second_int = int(input("Give second number"))
    print(gcd(first_int, second_int))


if __name__ == "__main__":
    main()

