print('№2. Узор: d.')
num_0 = 0  # счетчик
num_str = 6  # количество количество уровней "кирпичей"
while num_0 < num_str:
    num_0 += 1
    if num_0 % 2 == 1:
        print('\u001b[47m')
        print('\u001b[47m   \033[0m              ' * 20)
    else:
        print('\u001b[47m')
        print('\033[0m       \u001b[47m   \033[0m       ' * 20)
print('\u001b[47m')
print('\033[0m')