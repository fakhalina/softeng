from datetime import datetime #импортируем datetime
from math import sqrt #импортируем корень из модуля math

def main(**kwargs):
    """функия принимает произвольное количество аргументов"""
    for key in kwargs.items(): #перебираем все ключевые слова и их значения
        result = sqrt(key[1][0] ** 2 + key[1][1] ** 2)
        print(result) #вывод результата

if __name__ == '__main__': #точка входа
    start_time = datetime.now() #присваивание переменной текущее время
    main(
        one=[10, 3],
        two=[5, 4],
        three=[15, 13],
        four=[93, 53],
        five=[133,15]
    ) # передаем в main аргументы

time_costs = datetime.now() - start_time #вычитание из текущего времени стартовое
print(f'Время выполнения программы - {time_costs}')#вывод
