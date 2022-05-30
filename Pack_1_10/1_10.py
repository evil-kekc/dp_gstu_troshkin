import collections
from Pack_1_10.config import *
import math
from prettytable import PrettyTable
import Pack_1_8.p1_8
from Pack_1_9.p1_9 import Kz_list, Twt_list
import Pack_1_10.config


def calculations(*operations):
    Opr_list = []

    info_table = PrettyTable()
    info_table.field_names = ['Наименование', 'Tшт-к', 'mp', 'P', 'nз.ф.', 'Opi', 'Oпр.i']
    for info in operations:
        for num in info:
            nzph = num[2] / num[3]
            O = 0.8 / nzph
            Opr = math.ceil(O)

            Opr_list.append(Opr)

            info_table.add_row([num[0], num[1], num[2], num[3], nzph, O, Opr])

    info_table.add_row(['' for _ in range(7)])
    info_table.add_row(['ИТОГО:', '', '', '', '', '', sum(Opr_list)])
    print(f'Пункт 1.10')
    print(info_table)


all_operations = operation_1, operation_2, operation_3, operation_4, operation_5, operation_6
calculations(all_operations)
