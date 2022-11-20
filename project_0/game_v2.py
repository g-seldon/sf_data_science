"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    return count

def algo_predict(number: int = 1) -> int:
    """Угадываем число, каждый раз вдвое уменьшая диапазон, где оно находится.
       На каждом шаге делим текущий диапазон пополам и сравниваем его середину с загаданным числом.
       Если середина больше - берем меньшую половину диапазона, если меньше - берем большую.
       Если середина = загаданному числу, то поиск окончен. 
       Глубина поиска не должна превышать log_2(100)

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    up_bound = 100 #начальная верхняя граница
    dn_bound = 1 #начальная нижняя граница
    middle = 0 # переменная с серединой диапазона
    
    #print("Загаданное число: ", number)
    
    while True:
        count += 1
        middle = (up_bound + dn_bound) // 2  # новая середина
        #print("Новая середина: ", middle)
        if number > middle:
            dn_bound = middle + 1  # число в верхней половине - поднимаем нижнюю границу выше середины 
        elif number < middle:
            up_bound = middle - 1  # число в нижней половине - опускаем верхнюю границу ниже середины 
        else:
            break  # число = середине, выход из цикла
    
    #print("Число попыток: ", count)
    return count

def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(algo_predict)
