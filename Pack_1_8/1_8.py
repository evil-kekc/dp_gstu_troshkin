from Pack_1_8.config import *
from prettytable import PrettyTable


def calculations(*operations):
    Twtk_list = []

    info_table = PrettyTable()
    info_table.field_names = ['Операция', 'To', 'Toп', 'Tоб + Тот', 'Tшт', 'Tп-з', 'Tшт-к']
    for info in operations:
        for num in info:
            Tpz = num[2]
            To = num[1]
            n = 5000
            Tb = 0.285

            Top = To + Tb
            Ttex = (1.9 * Top) / 50
            Tob = (Top * 2.4) / 100
            Tot = (Top * 6) / 100
            Tobot = Tob + Tot + Ttex

            Twt = To + Tb + Tobot

            Twtk = (Tpz / n) + Twt
            Twtk_list.append(Twtk)

            info_table.add_row([num[0], To, Top, Tobot, Twt, Tpz, Twtk])

    info_table.add_row(['' for _ in range(7)])
    info_table.add_row(['ИТОГО:', '', '', '', '', '', sum(Twtk_list)])
    print(info_table)


all_operations = operation_1, operation_2, operation_3, operation_4, operation_5, operation_6
calculations(all_operations)