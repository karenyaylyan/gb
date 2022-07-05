class Cell:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        result = self.number - other.number
        if result > 0:
            return Cell(result)
        else:
            raise ValueError('The difference is negative')

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __floordiv__(self, other):
        return Cell(self.number // other.number)

    def __truediv__(self, other):
        return Cell(self.number // other.number)

    def make_order(self, number_in_row):
        result = ''
        rest_number = self.number
        full_row_count = self.number // number_in_row
        rest_count = self.number % number_in_row

        result = ('*'*number_in_row + '\n') * full_row_count
        result += '*'*rest_count + '\n'
        return result.rstrip()
