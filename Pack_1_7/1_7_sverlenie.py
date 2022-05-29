import math


"""Изменяемые параметры"""
t = 3.3
L_rez = 8.3
T = 35
S_z = 0.2
D = 6.6

"""Параметры по умолчанию"""
y = 0.55
q = 0.25

Cv = 14.7
m = 0.125
HB = 190
nv = 1.7
q1 = 1

Kmv = 0.8
Kuv = 1.15
Klv = 1
Kp = 1 ** nv
# print(f'Kp = {Kp}')

Cm = 0.021
x1 = 0
y1 = 0.8

"""Расчеты"""
Kv = Kmv * Kuv * Klv
# print(f'Kp = {Kv}')

V = (Cv * D**q * Kv) / (T**m * S_z**y)
print(f'\nСкорость резания V = {V}\n')

Mkp = 10 * Cm * D**q1 * S_z**y1 * Kp
# print(f'Mkp = {Mkp}\n')

n = (1000 * V) / (math.pi * D)
print(f'Число оборотов n = {n}\n')

N = (Mkp * n) / 9750
print(f'Мощность резания N = {N}\n')

Sm = S_z * n
print(f'Sm = {Sm}\n')

Lpx = L_rez + 5
To = Lpx / (S_z * n)
print(f'Основное время To = {To}')
