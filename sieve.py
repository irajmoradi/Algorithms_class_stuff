
def filter(nums, divisor):
    """
    removes all numbers in a list that are divisble by divisor
    Args:
        nums: List
        divisor: Int
    Examples:
        >>> filter([3, 6, 7, 8, 9], 4)
        [3, 6, 7, 9]
        >>> filter([4, 6, 8, 11, 13], 2)
        [11, 13]
        >>> filter([32, 33, 34, 35, 36], 36)
        [32, 33, 34, 35, 36]
    """

    ret_list = []
    for num in nums:
        if num > divisor:
            if num % divisor != 0:
                ret_list.append(num)
        if num <= divisor:
            ret_list.append(num)
    return ret_list


def main():
    primes_to_100 = range(1, 100)
    count = 1
    while count != len(primes_to_100):
        primes_to_100 = filter(primes_to_100, primes_to_100[count])
        count += 1
        print(primes_to_100)
    print(primes_to_100)


if __name__ == "__main__":
    main()
