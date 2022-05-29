import collections


nzn = 0.8
operations = collections.namedtuple('Операция', ['Наименование', 'Tшт', 'mp', 'P'])

operation_1 = operations(Наименование='010 Автоматная токарная с ЧПУ', Tшт=1.254, mp=0.063, P=1)

operation_2 = operations(
    Наименование='020 Токарная с ЧПУ', Tшт=1.232, mp=0.063, P=1)

operation_3 = operations(
    Наименование='030 Вертикально-сверлильная', Tшт=0.502, mp=0.026, P=1)

operation_4 = operations(
    Наименование='050 Алмазно-расточная', Tшт=0.626, mp=0.032, P=1)

operation_5 = operations(
    Наименование='080 Круглошлифовальная', Tшт=1.141, mp=0.058, P=1)

operation_6 = operations(
    Наименование='085 Токарная с ЧПУ', Tшт=0.357, mp=0.018, P=1)

