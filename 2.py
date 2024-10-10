print('№2. Узор: d.')
i = 0
while i < 6:
    i +=1
    if i % 2 == 1:
        print('\u001b[47m')
        print('\u001b[47m   \033[0m              ' * 20)
    else:
        print('\u001b[47m')
        print('\033[0m       \u001b[47m   \033[0m       ' * 20)
print('\u001b[47m')
print('\033[0m')