import collections

n = 200000
nzn = 0.8
operations = collections.namedtuple('Операция', ['Наименование', 'Tшт', 'mp', 'P'])

operation_1 = operations(Наименование='010 Автоматная токарная с ЧПУ', Tшт=1.252, mp=0.25, P=1)

operation_2 = operations(
    Наименование='020 Токарная с ЧПУ', Tшт=1.229, mp=0.25, P=1)

operation_3 = operations(
    Наименование='030 Вертикально-сверлильная', Tшт=0.5, mp=0.1, P=1)

operation_4 = operations(
    Наименование='050 Алмазно-расточная', Tшт=0.624, mp=0.13, P=1)

operation_5 = operations(
    Наименование='080 Круглошлифовальная', Tшт=1.139, mp=0.23, P=1)

operation_6 = operations(
    Наименование='085 Токарная с ЧПУ', Tшт=0.354, mp=0.07, P=1)

