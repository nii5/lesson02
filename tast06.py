key_dict = ('Название','Цена','Количество','eд')
list_prod = []
n = 0
def app_tuple(n):
    my_dict = {}
    for key in key_dict:
        value = input("Введите " + key + ': ')
        my_dict[key] = value

    my_tuple = (n, my_dict)
    return my_tuple

while True:
    y_n = input('Хотите добавить товар в базу y/n: ')
    if y_n.lower() == 'y':
        n += 1
        list_prod.append(app_tuple(n))
    else:
        break
list_prod = [
(1, {'Название': 'компьютер', 'Цена': 20000, 'Количество': 5, 'eд': 'шт.'}),
(2, {'Название': 'принтер', 'Цена': 6000, 'Количество': 2, 'eд': 'шт.'}),
(3, {'Название': 'сканер', 'Цена': 2000, 'Количество': 7, 'eд': 'шт.'})
]
new_dict ={}
for key in key_dict:
    new_list = []
    for val in list_prod:
        print(val)
        print(val[1].get(key))
        new_list.append(val[1].get(key))
        new_dict[key] = new_list

print(new_dict)