# Проверка на високосный год

year = int(input('Введите год: '))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    result = 'Високосный год'
else:
    result = 'Не високосный год'
print(result)