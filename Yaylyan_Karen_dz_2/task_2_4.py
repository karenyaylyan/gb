employees = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
             'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for employee in employees:
    *position, name = employee.split()
    print(f'Привет, {name.capitalize()}!')
