import copy
import math
from typing import List


def min(arr: list) -> float:
    """min
    :param: arr: list
    :return: float"""
    m = arr[0]
    for i in range(len(arr)):
        if arr[i] <= m:
            m = arr[i]
    return m


def max(arr: list) -> float:
    """max
    :param: arr: list
    :return: float"""
    m = arr[0]
    for i in range(len(arr)):
        if arr[i] >= m:
            m = arr[i]
    return m


def average(arr: list) -> float:
    """average
    :param: arr: list
    :return: float"""
    s = 0
    for i in range(len(arr)):
        s += arr[i]
    return s/len(arr)


def median(arr: List[float]) -> float:
    """ sort and median search
    :param: arr: list
    :return: float"""
    n = len(arr) - 1
    array = copy.copy(arr)
    array.sort()
    if len(arr) % 2 == 0:
        k = (array[n // 2] + array[n // 2 + 1]) // 2
    else:
        k = array[(n + 1) // 2]
    return k


def identical(arr: list) -> int:
    """maximum number of consecutive identical elements
    :param: arr: list
    :return: int"""
    length = 1
    m = 0
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            length += 1
        else:
            if length > m:
                m = length
    if m == 0:
        m = len(arr)
    return m


def monotone(arr: list) -> int:
    """maximum length of monotonous section
    :param: arr: list
    :return: int"""
    m = 0
    k = 0
    for i in range(len(arr) - 2):
        if (arr[i] >= arr[i + 1]) and (arr[i + 1] >= arr[i + 2]):
            m += 1
        if (arr[i] <= arr[i + 1]) and (arr[i + 1] <= arr[i + 2]):
            k += 1
    return k + 2 if k > m else m + 2


def rms(arr: list) -> float:
    """standard deviation
    :param: arr: list
    :return: float"""
    m = average(arr)
    s = 0
    for i in range(len(arr)):
        s += (arr[i] - m)*(arr[i] - m)
    c = math.sqrt(s / len(arr))
    return c


def test():
    """test
    :param: arr: list
    :return: bool"""
    array = [1, 2, 2, 7, 6]
    assert (min(array)) == 1
    assert (max(array)) == 7
    assert (average(array)) == 3.6
    assert (median(array)) == 2
    assert (monotone(array)) == 4
    assert (identical(array)) == 2
    assert (identical([2, 1, 2, 1, 4]) == 1)


def main():
    test()
    # n = int(input("Input length array: "))
    #     # arr = [0] * n
    #     # for i in range(n):
    #     #     print("arr[", i, "]=")
    #     #     arr[i] = int(input())
    #     # function1 = min(arr)
    #     # print("Mimimum =", function1)
    #     # function2 = max(arr)
    #     # print("Maximum =", function2)
    #     # function3 = average(arr)
    #     # print("Average =", function3)
    #     # function4 = median(arr)
    #     # print("Median =", function4)
    #     # function5 = identical(arr)
    #     # print("Identical =", function5)
    #     # function6 = rms(arr)
    #     # print("Standard deviation =", function6)
    #     # function7 = monotone(arr)
    #     # print("Monotone =", function7)


if __name__ == '__main__':
    main()