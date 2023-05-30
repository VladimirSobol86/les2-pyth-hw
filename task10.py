n = int(input("Введите общее число монет:  "))
o = 0
r = 0
for i in range(n):
    x = int(input("Введите номинал монеты 0 - орел, 1 - решка:   "))
    if x == 0:
        o += 1
    else:
        r += 1
if o > r:
    print(r)
else:
    print(o)