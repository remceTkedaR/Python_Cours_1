# przeszukiwanie zbioru obiektu sql1
# w poszukiwaniu obiektów takich samych jak w sql2

sql1 = [(1, 2), (444, 23), (13.4, 222)]
sql2 = [(1, 2), (13.4, 0)]

for key in sql2:
    if key in sql1:
        print(key, 'znaleziony')
    else:
        print(key, 'nieznaleziony')


# zebranie powtarzających się elementów w obu zbiorach danych

res = []
for x in sql1:
    if x in sql2:
        res.append(x)
print('powtarzające się elementy to ->', res)

