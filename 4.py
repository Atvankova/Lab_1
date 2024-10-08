print('№4. Диаграмма: Среднее по модулю первых 125 и вторых 125 чисел.')
massive = []
with open('sequence.txt', 'r') as file:
    for i in file:
        num_0 = float(i.strip())
        massive.append(abs(num_0))

sr_1 = sum(massive[0: 125]) / 125  #среднее по модулю первых 125 чисел
sr_2 = sum(massive[125:300]) / 125  #среднее по модулю вторых 125 чисел
sr = sum(massive) / len(massive)  #среднее всех чисел

num_1 = sr_1 * 100 / sr  #процентное отношение среднего по модулю первых 125 чисел (a) к среднему по модулю всех чисел
num_2 = sr_2 * 100 / sr  #процентное отношение среднего по модулю вторых 125 чисел (b) к среднему по модулю всех чисел

print('num_1', '\x1b[45;5;120m ' * int((sr_1 * 100 // sr)), '\x1b[m', round(num_1, 2), '%')
print()
print('num_2', '\x1b[45;5;120m ' * int((sr_2 * 100 // sr)), '\x1b[m', round(num_2, 2), '%')
print()
print('                10        20        30        40        50        60        70        80        90        100')
