class NotDigitException(Exception):
    def __init__(self, txt):
        self.txt = txt


number_lst = []

while True:
    try:
        number = input('Input number (or "stop" for end): ')
        if number == 'stop':
            break
        elif number.isdigit():
            number_lst.append(number)
        else:
            raise NotDigitException('value is not digit')
    except NotDigitException:
        pass

print(number_lst)
