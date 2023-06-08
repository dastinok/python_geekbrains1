# Работа с числами

number = int(input('Введите число от 1 до 999: '))

lenght = 0



if 0 < number < 10:
    lenght = 1
elif 9 < number < 100:
    lenght = 2
elif number < 0 or number > 999:
    lenght = -1
else:
    lenght = 3

print(lenght)

result = 0
if lenght == 1:
    result = number ** 2
elif lenght == 2:
    result = (number % 10) * (number // 10)
elif lenght == 3:
    a = number // 100
    b = number // 10 % 10
    c = number % 10
    result = c * 100 + b * 10 + a

print(f'Ваше число: {lenght} - значное, вы ввели число {number},  - {result}')

