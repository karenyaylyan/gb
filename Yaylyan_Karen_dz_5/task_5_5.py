src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
temp_set = set()

for el in src:
    if el in temp_set:
        temp_set.discard(el)
    else:
        temp_set.add(el)
result = [el for el in src if el in temp_set]
print(result)
