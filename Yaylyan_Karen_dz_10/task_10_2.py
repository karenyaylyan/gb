from abc import ABC, abstractmethod


class Outfit(ABC):
    @abstractmethod
    def add_clothes(self):
        pass

    @abstractmethod
    def common_consuption(self):
        pass


class Suit:
    def __init__(self, H):
        self.consuption = 2*H + 0.3


class Coat:
    def __init__(self, V):
        self.consuption = V/6.5 + 0.5


class Clothes:
    def __init__(self):
        self.clothes = []

    def add_clothes(self, clothes_name, parameter):
        if clothes_name == 'Suit':
            self.clothes.append(Suit(parameter))
        else:
            self.clothes.append(Coat(parameter))

    @property
    def common_consuption(self):
        result = 0
        for el in self.clothes:
            result += el.consuption
        return result


c = Clothes()
c.add_clothes('Suit', 1)
c.add_clothes('Suit', 2)
c.add_clothes('Coat', 1)
c.add_clothes('Coat', 2)
print(c.common_consuption)
