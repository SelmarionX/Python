base_csv = 'base.csv'

def input_data():
    import csv
    head = ['Фамилия', 'Имя', 'Отчество', 'Телефон', 'ID', 'Должность']
    values = []
    for i in head:
        enter = input(f'Введите {i} ')
        if i == head[3] or i == head[4]  :
            if enter.isdigit() == False:
                print('Поле должно быть числом')
                print()

                break
        else:
            if enter.isdigit() == True:
                print('Поле должно быть текстом')
                break
        values.append(enter)
    if len(values) == 6:
        with open(base_csv, 'a', encoding="utf-8") as file:
            writer = csv.writer(file, lineterminator='\n', delimiter=';')
            writer.writerow(values)