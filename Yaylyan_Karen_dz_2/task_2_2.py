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
new_lst = []

for element in lst:
    if is_integer(element):
        new_element = fill_zero(element)
        new_lst.extend(['"', new_element, '"'])
    else:
        new_lst.append(element)
print(new_lst)

string = ''
flag_in_number = False
for token in new_lst:
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
