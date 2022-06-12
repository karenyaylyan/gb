import sys
import os

with open('bakery.csv', 'r', encoding='utf-8') as f:
    sales = []
    for line in f:
        sales.append(line.strip())

index = int(sys.argv[1]) - 1
if index < 0 or index > len(sales) - 1:
    print('Введите допустимый номер')
    os._exit(1)

sales[index] = sys.argv[2]
with open('bakery.csv', 'w', encoding='utf-8') as f:
    for sale in sales:
        f.write(f'{sale}\n')
