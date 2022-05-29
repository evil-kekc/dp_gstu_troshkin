import math


"""Изменяемые параметры"""
t = 1.9
L_rez = 2.5
T = 30
S_z = 0.2
D = 62

"""Параметры по умолчанию"""
x = 0.15
y = 0.2

Cv = 292
m = 0.2
HB = 190
nv = 1.7
Knv = 0.8
Kuv = 1.15

Cp = 92
x1 = 1
y1 = 0.75
n1 = 0
t1 = 1

Kmp = (HB / 190) ** n1
K_1p = 1  # Kφp
K_2p = 1  # Kγp
K_3p = 1  # Kλp
K_4p = 1  # Krp


"""Расчеты"""
Kmv = (190 / HB) ** nv
# print(f'Kmv = {Kmv}')

Kv = Kmv * Knv * Kuv
# print(f'Kv = {round(Kv, 2)}')

V = (Cv * Kv) / (T**m * t**x * S_z**y)
print(f'\nСкорость резания V = {V}\n')

Kp = Kmp * K_1p * K_2p * K_3p * K_4p
# print(f'Kp = {round(Kp, 2)}')

Pz = 10 * Cp * t1**x1 * S_z**y1 * V**n1 * Kp
# print(f'Pz = {round(Pz, 2)}')

N = (Pz * V) / (1020 * 60)
print(f'Мощность N = {N}\n')

n = (1000 * V) / (math.pi * D)
print(f'n = {n}\n')

Sm = S_z * n
# print(f'Sm = {round(Sm, 2)}')

L_px = L_rez + 5
# print(f'Длина рабочего хода Lpx = {L_px}\n')

To = L_px / (S_z * n)
print(f'Основное время To = {To}')
