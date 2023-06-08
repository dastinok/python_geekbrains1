# Таблица умножения
BEGIN = 1
END = 10

for num in range(BEGIN, END):
    mult1 = BEGIN * num
    mult2 = (BEGIN + 1) * num
    mult3 = (BEGIN + 2) * num
    mult4 = (BEGIN + 3) * num
    mult5 = (BEGIN + 4) * num

    print(f'{BEGIN} * {num} = {mult1}\t {BEGIN+1} * {num} = {mult2}\t\t {BEGIN+2} * {num} = {mult3}\t\t' +

          f'{BEGIN+3} * {num} = {mult4}\t\t {BEGIN+4} * {num} = {mult5}')

print('')
for num in range(BEGIN, END):
    mult6 = (BEGIN + 5) * num
    mult7 = (BEGIN + 6) * num
    mult8 = (BEGIN + 7) * num
    mult9 = (BEGIN + 8) * num


    print(f'{BEGIN+5} * {num} = {mult6}\t {BEGIN + 6} * {num} = {mult7}\t\t {BEGIN + 7} * {num} = {mult8}\t\t' +

          f'{BEGIN + 8} * {num} = {mult9}')




