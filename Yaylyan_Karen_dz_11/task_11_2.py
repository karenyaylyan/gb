class ZeroDivisionException(Exception):
    def __init__(self, txt):
        self.txt = txt


numerator, denominator = map(int, input('Введите 2 числа: ').split())

try:
    if denominator == 0:
        raise ZeroDivisionException('division by zero!')
    else:
        print(numerator / denominator)
except ZeroDivisionException:
    print('На ноль делить нельзя')
