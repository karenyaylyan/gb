import csv
import json
import os
import sys

if len(sys.argv) != 4:
    print('Неверное число аргументов: argv != 4')
    os._exit(1)

with open(sys.argv[1], 'r', encoding='utf-8') as f:
    users = []
    for line in csv.reader(f):
        users.append(' '.join(line))

with open(sys.argv[2], 'r', encoding='utf-8') as f:
    hobby = []
    for line in csv.reader(f):
        hobby.append(line)

user_hobby = {}

for user, hob in zip(users, hobby):
    user_hobby[user] = hob

if len(users) > len(hobby):
    for i in range(len(hobby), len(users)):
        user_hobby[users[i]] = None

with open(sys.argv[3], 'w', encoding='utf-8') as f:
    json.dump(user_hobby, f, ensure_ascii=False)

with open(sys.argv[3], 'r', encoding='utf-8') as f:
    user_hobby_load = json.load(f)

if user_hobby == user_hobby_load:
    print('Сохраненные данные совпадают с изначальными')

if len(users) < len(hobby):
    os._exit(1)
