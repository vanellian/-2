list_ = [3, 4, 8, 9, 6, 6, 2, 4, 3, 3, 1]

# TODO завести отдельные счетчики для четных и нечетных чисел

# TODO с помощью одного цикла перебрать все числа и посчитать количество четных и нечетных

# TODO вывести каких чисел больше

cht = 0
n_cht = 0

for i in range(len(list_)):
    if list_[1] % 2 == 0:
        cht += 1
    else:
        n_cht += 1

if cht > n_cht:
    print("Четных чисел больше")
else:
    print("Нечетных чисел больше")