def num_translate_adv(number_en):
    dict_of_numbers = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять',
    }

    number_ru = dict_of_numbers.get(number_en.lower())

    if number_ru is not None and number_en.istitle():
        return number_ru.title()
    elif number_ru is not None and number_en.islower():
        return number_ru

    return None
