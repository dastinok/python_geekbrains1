# Написать программу, которая будет выводить в консоль ёлочку заданной высоты


height = int(input('Введите высоту елки: '))

for i in range(1, height + 1):
    for j in range(1, height-i+1):
        print(' ', end='')
    for k in range(1, 2*i):
        print('*', end='')
    print()