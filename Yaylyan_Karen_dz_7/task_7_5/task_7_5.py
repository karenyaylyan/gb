import os
import json
import django
from collections import defaultdict

root_dir = django.__path__[0]
files_quantity = defaultdict(int)
files_extensions_list = defaultdict(set)

for root, dirs, files in os.walk(root_dir):
    for file in files:
        ext = file.rsplit('.', maxsplit=1)[-1].lower()
        file_size = os.stat(os.path.join(root, file)).st_size
        if file_size == 0:
            files_quantity[0] += 1
            files_extensions_list[0].add(ext)
        else:
            border = 10
            while file_size > border:
                border *= 10
            files_quantity[border] += 1
            files_extensions_list[border].add(ext)

dir_statistic = {}

for key in files_quantity:
    dir_statistic[key] = (files_quantity[key], list(files_extensions_list[key]))

print(dir_statistic)
with open('django_summary.json', 'w', encoding='utf-8') as f:
    json.dump(dir_statistic, f)
