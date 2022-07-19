class Complex:
    def __init__(self, real, image):
        self.real = real
        self.image = image

    def __add__(self, other):
        return Complex(self.real + other.real, self.image + other.image)

    def __mul__(self, other):
        new_real = self.real*other.real - self.image*other.image
        new_image = self.real*other.image + self.image*other.real
        return Complex(new_real, new_image)

    def __eq__(self, other):
        return self.real == other.real and self.image == other.image


a = Complex(2, 3)
b = Complex(5, 1)
assert a + b == Complex(7, 4)

a = Complex(1, 3)
b = Complex(-5, -2)
assert a * b == Complex(1, -17)
