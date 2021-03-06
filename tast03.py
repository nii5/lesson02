'''
3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
'''
months = ['Январь', 'Февраль', 'Март','Апрель', 'Май','Июнь','Июль','Авгус','Сентябрь','Октябрь', 'Ноябрь', 'Декабрь']

seasons = {'Зима': (1, 2, 12),
           'Весна': (3, 4, 5),
           'Лето': (6, 7, 8),
           'Осень': (9, 10, 11)}

month = int(input('Введите номер месяца: '))
for key in seasons.keys():
    if month in seasons[key]:
        print(f'Ваш месяц {months[month-1]} относится к времени года {key}')