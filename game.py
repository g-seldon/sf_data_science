"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""

import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # предполагаемое число
        if number == predict_number:
            break # выход из цикла, если угадали
    return(count)

if __name__ == '__main__':
    print(f'Количество попыток: {random_predict()}')

# number = np.random.randint(1,101)
# count = 0

# while True:
#     count += 1
#     predict_number = int(input("Угадай число от 1 до 100: "))
#     if predict_number > number:
#         print("Число должно быть меньше!")
#     elif predict_number < number:
#         print("Число должно быть больше!")
#     else:
#         print(f"Вы угадали число! Это число = {number}, за {count} попыток")
#         break # конец игры, выход из цикла
