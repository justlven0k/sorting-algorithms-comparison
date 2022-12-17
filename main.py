"""!@package main
Основной модуль.
"""
from time import time, sleep
from os import system
from threading import Thread
from random import randint
import matplotlib.pyplot as plt
from typeguard import typechecked
from typing import Callable


from sorting_algorithms import *

graph_drawing = False
max_element_value_in_array = 500
size_of_blocks = 0.02
sorting_algorithms_info = {
    1: {
        "name": "Bubble sort",
        "function": bubble_sort,
        "max range": 10000
    },
    2: {
        "name": "Merge sort",
        "function": merge_sort,
        "max range": 100000
    },
    3: {
        "name": "Comb sort",
        "function": comb_sort,
        "max range": 100000
    },
    4: {
        "name": "Shell sort",
        "function": shell_sort, 
        "max range": 100000
    },
    5: {
        "name": "Bead sort",
        "function": bead_sort, 
        "max range": 2500
    }
}


@typechecked
def main() -> None:
    """!
    Основной интерфейс для взаимодействия с пользователем. 
    Генерация начальных значений для алгоритмо сортировки.

    @return: None
    """

    global graph_drawing
    global sorting_algorithms_info
    global max_element_value_in_array
    global size_of_blocks

    print("Алгоритмы сортировки на выбор:")
    for i in sorting_algorithms_info.keys():
        print("{} -> {}".format(i, sorting_algorithms_info[i]["name"]))
    

    try:
        selected_algorithms = input("Перечислите необходимые алгоритмы сортировки (через запятую): ").split(',')
        selected_algorithms = set(map(int, selected_algorithms))
        for i in selected_algorithms:
            if not sorting_algorithms_info.get(i, 0):
                print("Неправильный номер алгоритма!")
                quit()

    except ValueError:
        print("Неправильный формат ввода!")
        quit()


    graph_drawing = True
    loading_screen_thread = Thread(target=loading_screen)
    loading_screen_thread.start()

    selected_labels = [sorting_algorithms_info[i]["name"] for i in selected_algorithms]
    colors = [get_random_hex_color() for i in range(len(selected_algorithms))]
    x_data = []
    y_data = []

    for i in selected_algorithms:
        max_elements_number = sorting_algorithms_info[i]["max range"]
        current_algorithm = sorting_algorithms_info[i]["function"]
        
        x_data.append(list(range(1, max_elements_number, int(max_elements_number * size_of_blocks))))
        y_data.append([])

        for j in x_data[-1]:
            y_data[-1].append(get_algorithm_time(current_algorithm, [randint(1, max_element_value_in_array) for k in range(j)]))

    graph_drawing = False
    draw_graphs(x_data, y_data, selected_labels, colors)


@typechecked
def loading_screen() -> None:
    """!
    Экран загрузки.

    @return: None
    """

    global graph_drawing

    loading_string = "Рисуем ваш график......"
    char_number = 0

    while graph_drawing:
        system("cls")

        if loading_string[char_number] != '.':
            print(loading_string[:char_number] + loading_string[char_number:].capitalize())

        else:
            print(loading_string[:char_number] + ' ' + loading_string[char_number + 1:])

        char_number += 1
        char_number %= len(loading_string)
        sleep(0.1)

    system("cls")


@typechecked
def get_random_hex_color() -> str:
    """!
    Генерация случайного цвета.

    @return: цвет в формате HEX
    """
    return '#' + str(hex(randint(16**5, 16**6)))[2:]


@typechecked
def get_algorithm_time(sorting_algorithm: Callable, algorithm_input: list[int]) -> float:
    """!
    Измерение времени работы алгоритма.

    @param sorting_algorithm: алгоритм сортировки
    @param algorithm_input: входные данные для алгоритма сортировки

    @return: время работы алгоритма в секундах
    """
    start = time()

    sorting_algorithm(algorithm_input)

    end = time()
    return end - start
        
    
@typechecked
def draw_graphs(x_data: list[list[int]], y_data: list[list[float]], labels: list[str], colors: list[str]) -> None:
    """!
    Рисования графиков.

    @param x_data: количество элементов в массиве
    @param y_data: время, необходимое для сортировки массива
    @param labels: названия алгоритмов сортировки
    @param colors: цвета для графиков функций

    @exception IndexError в случае неверных входных данных

    @return: None
    """

    if len(x_data) != len(y_data):
        raise IndexError("Неверные входные параметры!")
    
    for i in range(len(x_data)):
        plt.plot(x_data[i], y_data[i], color=colors[i], label=labels[i])

    plt.xlabel("Number Of Elements")
    plt.ylabel("Time")

    plt.title("Sorting Algorithms Comparison")

    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()