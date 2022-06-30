class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_of_asphalt(self, mass_one_square=25, thickness_sm=5):
        return self._length * self._width * mass_one_square * thickness_sm / 100
