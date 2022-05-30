from matplotlib import pyplot as plt
from Pack_1_9.config import *
import math
from prettytable import PrettyTable

global Kz_list, Twt_list


def calculations(*operations):
    global Kz_list, Twt_list
    Kz_list = []
    Ko_list = []
    Km_list = []
    names = []
    To_list = []
    Twt_list = []

    info_table = PrettyTable()
    info_table.field_names = ['Операция', 'Модель', 'N', 'To', 'Tшт', 'mp', 'mпр', 'Kз', 'Kо', 'Nпр', 'Nрез', 'Kм']
    for info in operations:
        for num in info:
            mp = (num[4] * num[2]) / (60 * 2050 * 0.8)
            mpr = math.ceil(mp)

            Kz = mp / mpr

            Ko = num[3] / num[4]

            Km = num[6] / num[5]

            Kz_list.append(Kz)
            Ko_list.append(Ko)
            Km_list.append(Km)
            names.append(num[1])
            To_list.append(num[3])
            Twt_list.append(num[4])

            info_table.add_row([num[0], num[1], num[2], num[3], num[4], mp, mpr, Kz, Ko, num[5], num[6], Km])

    plt.bar(names, Kz_list)
    plt.title(label='Kз', loc='center')
    plt.show()

    plt.bar(names, Ko_list)
    plt.title(label='Kо', loc='center')
    plt.show()

    plt.bar(names, Km_list)
    plt.title(label='Kм', loc='center')
    plt.show()

    info_table.add_row(['' for _ in range(12)])
    info_table.add_row(['ИТОГО:', '', '', sum(To_list), sum(Twt_list), '', '', sum(Kz_list), sum(Ko_list), '', '',
                        sum(Km_list)])
    print(f'Пункт 1.9')
    print(info_table, '\n')


all_operations = operation_1, operation_2, operation_3, operation_4, operation_5, operation_6
calculations(all_operations)
