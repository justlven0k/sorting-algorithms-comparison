"""!@package sorting_algorithms_test
Модуль со всеми тестами алгоритмов сортировки.
"""
from sorting_algorithms import *
from random import randint


def test_reversed_array():
    """!
    Проверка сортировок на перевернутом массиве.

    @return: None
    """
    
    array = [i for i in range(1000, -1, -1)]
    sorted_array = sorted(array)

    assert bubble_sort(array) == sorted_array
    assert shell_sort(array) == sorted_array
    assert merge_sort(array) == sorted_array
    assert comb_sort(array) == sorted_array
    assert bead_sort(array) == sorted_array


def test_zero_length_array():
    """!
    Проверка сортировок на пустом массиве.

    @return: None
    """

    array = []
    sorted_array = sorted(array)

    assert bubble_sort(array) == sorted_array
    assert shell_sort(array) == sorted_array
    assert merge_sort(array) == sorted_array
    assert comb_sort(array) == sorted_array
    assert bead_sort(array) == sorted_array


def test_one_length_array():
    """!
    Проверка сортировок на массиве с 1им элементом.

    @return: None
    """

    array = [randint(1, 100)]
    sorted_array = sorted(array)

    assert bubble_sort(array) == sorted_array
    assert shell_sort(array) == sorted_array
    assert merge_sort(array) == sorted_array
    assert comb_sort(array) == sorted_array
    assert bead_sort(array) == sorted_array


def test_only_zeros_array():
    """!
    Проверка сортировок на массиве, состоящем из нулей.

    @return: None
    """

    array = [0] * 100
    sorted_array = sorted(array)

    assert bubble_sort(array) == sorted_array
    assert shell_sort(array) == sorted_array
    assert merge_sort(array) == sorted_array
    assert comb_sort(array) == sorted_array
    assert bead_sort(array) == sorted_array


def test_ordered_array():
    """!
    Проверка сортировок на отсортированном массиве.

    @return: None
    """
    
    array = list(range(100))
    sorted_array = sorted(array)

    assert bubble_sort(array) == sorted_array
    assert shell_sort(array) == sorted_array
    assert merge_sort(array) == sorted_array
    assert comb_sort(array) == sorted_array
    assert bead_sort(array) == sorted_array


def test_negative_elements_array():
    """!
    Проверка сортировок на массиве с отрицательными числами.

    @return: None
    """

    array = list(range(-100, 100))
    sorted_array = sorted(array)

    assert bubble_sort(array) == sorted_array
    assert shell_sort(array) == sorted_array
    assert merge_sort(array) == sorted_array
    assert comb_sort(array) == sorted_array


def test_same_elements_array():
    """!
    Проверка сортировок на массиве с одинаковыми элементами.

    @return: None
    """
    array = [randint(0, 10000)] * 100
    sorted_array = sorted(array)

    assert bubble_sort(array) == sorted_array
    assert shell_sort(array) == sorted_array
    assert merge_sort(array) == sorted_array
    assert comb_sort(array) == sorted_array
    assert bead_sort(array) == sorted_array


def test_random_elements_array():
    """!
    Проверка сортировок на случайных массивах.

    @return: None
    """
    for i in range(250):
        array = [randint(0, 500) for j in range(100)]
        sorted_array = sorted(array)

        assert bubble_sort(array) == sorted_array
        assert shell_sort(array) == sorted_array
        assert merge_sort(array) == sorted_array
        assert comb_sort(array) == sorted_array
        assert bead_sort(array) == sorted_array