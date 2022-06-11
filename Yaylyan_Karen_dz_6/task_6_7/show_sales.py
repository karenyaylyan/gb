import sys

with open('bakery.csv', 'r', encoding='utf-8') as f:
    if len(sys.argv) == 1:
        for line in f:
            print(line.strip())
    elif len(sys.argv) == 2:
        for i, line in enumerate(f):
            if i >= int(sys.argv[1]) - 1:
                print(line.strip())
    elif len(sys.argv) == 3:
        for i, line in enumerate(f):
            if i >= int(sys.argv[1]) - 1 and i <= int(sys.argv[2]) - 1:
                print(line.strip())  
