import math

print(math.cos(0))
print(math.log10(100))

import random
print(random.randint(1, 20)) # 1부터 20사이의 랜덤한 정수
print(random.uniform(0, 1)) # 0과 1사이의 랜덤한 소수

import datetime
today = datetime.datetime.now()
print(today)

print(today.strftime("%A, %B %dth %Y"))

pi_day = datetime.datetime(2020, 3, 14, 13, 6, 15)
print(pi_day)
print(today - pi_day)

import os
print(os.getlogin())
print(os.getcwd())
print(os.getpid())

import os.path
print(os.path.abspath('..'))
print(os.path.relpath('/Users/codeit/PycharmProjects'))
print(os.path.join('/Users/codeit/PycharmProjects', 'standard_modules'))

import re # re는 클래스로 되어있는가?
pattern = re.compile('^[A-Za-z]+$')
print(pattern.match('I'))
print(pattern.match('love'))
print(pattern.match('python3'))

print()

pattern = re.compile('.*/d+')
print(pattern.match('I'))
print(pattern.match('love'))
print(pattern.match('python3'))

import pickle
obj = {'my': 'dictionary'}

with open('filename.pickle', 'wb') as f:
    pickle.dump(obj, f)

with open('filename.pickle', 'rb') as f:
    obj = pickle.load(f)
print(obj)

import json
obj = {"my":"dictionary"}

with open('filename.json', 'w') as f:
    json.dump(obj, f)

with open('filename.json', 'r') as f:
    obj = json.load(f)
print(obj)

import copy

a = [1, 2, 3]
b = a
c = a[:]
d = copy.copy(a)
a[0] = 4
print(a, b, c, d)

import sqlite3
conn = sqlite3.connect('example.db')

c = conn.cursor()
c.execute('''SELECT ... FROM ... WHERE ...''')

rows = c.fetchall()
for row in rows:
    print(row)

conn.close()
