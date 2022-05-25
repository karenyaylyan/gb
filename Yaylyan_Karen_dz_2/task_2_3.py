def is_integer(value):
    try:
        int(value)
    except ValueError:
        return False
    return True


def fill_zero(element):
    if element[0] == '+' or element[0] == '-':
        return element.zfill(3)
    else:
        return element.zfill(2)


lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была',
       '+5', 'градусов']

i = 0
while i < len(lst):
    if is_integer(lst[i]):
        lst[i] = fill_zero(lst[i])
        lst.insert(i, '"')
        lst.insert(i+2, '"')
        i += 3
    else:
        i += 1
print(lst)

string = ''
flag_in_number = False
for token in lst:
    if is_integer(token):
        string += token
    elif token == '"' and not flag_in_number:
        flag_in_number = True
        string += token
    elif token == '"' and flag_in_number:
        flag_in_number = False
        string += token + ' '
    else:
        string += token + ' '
string = string.rstrip()
print(string)
