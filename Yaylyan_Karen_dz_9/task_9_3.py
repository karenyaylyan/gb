class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


employee = Position('Ivan', 'Petrov', 'manager', 100_000, 70_000)

assert employee.get_full_name() == 'Ivan Petrov', 'Неверное имя'
assert employee.get_total_income() == 170_000, 'Неверный доход'
