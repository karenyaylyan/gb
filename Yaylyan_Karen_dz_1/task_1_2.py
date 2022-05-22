def is_div_7(number):
    sum_of_digits = 0
    while number > 0:
        sum_of_digits += number % 10
        number //= 10
    return sum_of_digits % 7 == 0


def sum_of_numbers_div_7(numbers):
    sum_of_numbers = 0
    for number in numbers:
        if is_div_7(number):
            sum_of_numbers += number
    return sum_of_numbers


third_power_numbers = [i**3 for i in range(1, 1001, 2)]
sum_of_numbers_1 = sum_of_numbers_div_7(third_power_numbers)
print(f'Сумма чисел a)', sum_of_numbers_1)

for i in range(len(third_power_numbers)):
    third_power_numbers[i] += 17
sum_of_numbers_2 = sum_of_numbers_div_7(third_power_numbers)
print(f'Сумма чисел b)', sum_of_numbers_2)
