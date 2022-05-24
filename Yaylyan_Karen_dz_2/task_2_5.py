def print_prices(prices):
    is_first = True
    for price in prices:
        if not is_first:
            print(', ', end='')
        else:
            is_first = False
        rub = int(price)
        kk = int(price*100) - rub*100
        print(f'{rub} руб {kk:02d} коп', end='')
    print()


prices = [57.8, 46.51, 97, 0, 5.4, 5.04, 0.43, 11, 123, 43.2]
print('Цены на товары: ', end='')
print_prices(prices)
id_before = id(prices)

prices.sort()
print('Цены по возрастанию: ', end='')
print_prices(prices)
id_after = id(prices)

if id_before == id_after:
    print('Объект списка после сортировки тот же')

prices = list(reversed(prices))
id_new = id(prices)

if id_after != id_new:
    print('Был создан новый список с сортировкой по убыванию')

print('Цены на 5 самых дорогих товаров: ', end='')
print_prices(prices[4::-1])
