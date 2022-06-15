import os
import django
from collections import defaultdict

root_dir = django.__path__[0]
dir_statistic = defaultdict(int)

for root, dirs, files in os.walk(root_dir):
    for file in files:
        file_size = os.stat(os.path.join(root, file)).st_size
        if file_size == 0:
            dir_statistic[0] += 1
        else:
            border = 10
            while file_size > border:
                border *= 10
            dir_statistic[border] += 1

dir_statistic = dict(dir_statistic)
print(dir_statistic)
