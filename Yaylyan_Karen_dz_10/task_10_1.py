class Matrix:
    def __init__(self, list_of_lists):
        self.data = list_of_lists

    def __str__(self):
        is_first = True
        result = ''

        for row in self.data:
            if is_first:
                is_first = False
            else:
                result += '\n'
            result += "|{}|".format(' '.join(map(str, row)))

        return result

    def __add__(self, other):
        result = [
                    [
                        self.data[i][j] + other.data[i][j]
                        for j in range(len(self.data[i]))
                    ]
                    for i in range(len(self.data))
        ]

        return Matrix(result)
