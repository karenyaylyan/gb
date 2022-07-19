from collections import defaultdict


class Storage:
    def __init__(self):
        self.data = defaultdict(list)

    def accept(self, equipment):
        self.data[type(equipment).__name__].append(equipment)

    def send(self, equipment_name, number):
        Storage.validate_number(number)
        Storage.validate_equipment_name(equipment_name)

        if (equipment_name in self.data and
                len(self.data[equipment_name]) >= number):
            del self.data[equipment_name][:number]
            print(f'{number} {equipment_name} send to division')
        else:
            print(f'there are no {number} {equipment_name} for sending')

    @staticmethod
    def validate_number(number):
        if not isinstance(number, int):
            raise Valuerror('number type is not "int"')

    @staticmethod
    def validate_equipment_name(equipment_name):
        if (equipment_name != 'Printer' and
                equipment_name != 'Scanner' and
                equipment_name != 'Copier'):
            raise Valuerror('wrong equipment name')


class Office_Equipment:
    COUNT = 0

    def __init__(self, price, color):
        Office_Equipment.COUNT += 1

        self.u_id = Office_Equipment.COUNT
        self.price = price
        self.color = color

    @staticmethod
    def validate_color(color):
        if not isinstance(color, str):
            raise Valuerror('color type is not "str"')

    @staticmethod
    def validate_price(price):
        if not isinstance(price, int) or not isinstance(price, float):
            raise Valuerror('price type is not "int" or "float"')


class Printer(Office_Equipment):
    def print(self, txt):
        print(f'print text: {txt}')


class Scanner(Office_Equipment):
    def scan(self, txt):
        print(f'scan text: {txt}')


class Copier(Office_Equipment):
    def copy(self, txt):
        print(f'copy text: {txt}')


st = Storage()
p1 = Printer(1000, 'red')
s1 = Scanner(2000.5, 'black')
p2 = Printer(3000, 'blue')
p3 = Printer(4000, 'white')
c1 = Copier(5000, 'green')

p1.print('printing txt')
s1.scan('scanning doc')
c1.copy('copying doc')

st.accept(p1)
st.accept(s1)
st.accept(p2)
st.accept(p3)
st.accept(c1)
st.send('Printer', 2)
st.send('Scanner', 1)
