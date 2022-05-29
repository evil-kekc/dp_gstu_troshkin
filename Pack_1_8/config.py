import collections

operations = collections.namedtuple('Операция', ['Наименование', 'To', 'Tпз'])

operation_1 = operations(
    Наименование='010 Автоматная токарная с ЧПУ', To=0.83, Tпз=16)

operation_2 = operations(
    Наименование='020 Токарная с ЧПУ', To=0.81, Tпз=16)

operation_3 = operations(
    Наименование='030 Вертикально-сверлильная', To=0.16, Tпз=16)

operation_4 = operations(
    Наименование='050 Алмазно-расточная', To=0.27, Tпз=16)

operation_5 = operations(
    Наименование='080 Круглошлифовальная', To=0.73, Tпз=12)

operation_6 = operations(
    Наименование='085 Токарная с ЧПУ', To=0.03, Tпз=16)

