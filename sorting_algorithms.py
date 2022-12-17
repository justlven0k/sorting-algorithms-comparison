"""!@package sorting_algorithms
Модуль со всеми алгоритмами сортировки.
"""
from typeguard import typechecked
from itertools import zip_longest


@typechecked
def bubble_sort(array: list[int]) -> list[int]:
    """!
    Сортировка пузырьком.

    @param array: массив целых чисел

    @return: отсортированный массив
    """

    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[j] < array[i]:
                array[i], array[j] = array[j], array[i]

    return array


@typechecked
def comb_sort(array: list[int]) -> list[int]:
    """!
    Сортировка расческой.

    @param array: массив целых чисел

    @return: отсортированный массив
    """

    step = len(array)

    while step > 1:
        step = int(step / 1.247)
        i = 0
        while i + step < len(array):
            if array[i] > array[i + step]:
                array[i], array[i + step] = array[i + step], array[i]
            i += 1
    
    return array


@typechecked
def shell_sort(array: list[int]) -> list[int]:
    """!
    Сортировка Шелла.

    @param array: массив целых чисел

    @return: отсортированный массив
    """

    step = len(array) // 2

    while step:
        for i, el in enumerate(array):
            while i >= step and array[i - step] > el:
                array[i] = array[i - step]
                i -= step

            array[i] = el

        step //= 2

    return array


@typechecked
def merge_sort(array: list[int]) -> list[int]:
    """!
    Сортировка слиянием.

    @param array: массив целых чисел

    @return: отсортированный массив
    """

    i = 1
    while i < len(array):
        j = 0
        while j < len(array) - i:
            left = j
            middle = j + i
            right = min(j + 2*i, len(array))
            
            result = []
            left_pointer = left
            right_pointer = middle
            while left_pointer < middle and right_pointer < right:
                if array[left_pointer] < array[right_pointer]:
                    result += [array[left_pointer]]
                    left_pointer += 1

                else:
                    result += [array[right_pointer]]
                    right_pointer += 1

            result += array[left_pointer : middle]
            result += array[right_pointer : right]
            array[left : right] = result

            j += 2*i
        i *= 2

    return array


@typechecked
def bead_sort(array: list[int]) -> list[int]:
    """!
    Бисерная сортировка.

    @param array: массив целых чисел

    @return: отсортированный массив
    """

    maxi = max(array) if len(array) else 0

    result = []
    transposed_array = [0] * maxi

    for num in array:
        transposed_array[:num] = [n + 1 for n in transposed_array[:num]]

    for i in range(len(array)):
        result.append(sum(n > i for n in transposed_array))

    return result[::-1]