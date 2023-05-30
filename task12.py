x = int(input("Введите сумму чисел: "))
y = int(input("Введите произведение чисел: "))
for i in range(1000):
    for j in range(1000):
        if i + j == x and i * j == y:
            print("Первое число: ", i, "Второе число: ", j)
           