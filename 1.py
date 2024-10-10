print('№1. Страна: Польша.')


def flagg(height, width):
    if height % 2 == 0:
        average_1 = height // 2
        average_2 = height // 2
        while average_1 > 0:
            print('\u001b[47m ' * width, '\x1b[m')
            average_1 -= 1
        while average_2 > 0:
            print('\u001b[41m ' * width, '\x1b[m')
            average_2 -= 1
    else:
        print('Высота должна быть четным числом, поскольку флаг Польши зеркален относительно линии горизонта.')


flagg(2, 12)
