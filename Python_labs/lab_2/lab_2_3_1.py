import csv

filename = 'files/players.csv'
results = open('files/results.csv', 'w', newline="", encoding='utf-8')
columns = ["Спортсмен", "Место"]
writer = csv.DictWriter(results, fieldnames=columns)
writer.writeheader()
list_with_dict = []
list_with_col = []
with open(filename, "r", newline="", encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for r in reader:
        list_with_dict.append(r)
        list_with_col.append(r['Количество побед'])
new_list = []
col_list = []
dop = {"Количество": {0: []}}
print(list_with_dict)
for i in range(len(list_with_dict)):
    if list_with_col.count(list_with_dict[i]['Количество побед']) != 1:
        key = list_with_dict[i]['Количество побед']
        if key in dop['Количество'].keys():
            dop['Количество'][key].append(list_with_dict[i]['Доп. показатель'])
        else:
            dop['Количество'][key] = [list_with_dict[i]['Доп. показатель']]

print(dop)
while len(new_list) != len(list_with_dict):
    for i in range(len(list_with_dict)):
        if len(list_with_col) != 0:
            if list_with_dict[i]['Количество побед'] == max(list_with_col):
                if list_with_dict[i]['Количество побед'] in dop['Количество'].keys() and list_with_dict[i][
                    'Доп. показатель'] == max(dop['Количество'][list_with_dict[i]['Количество побед']]):
                    new_list.append(list_with_dict[i])
                    col_list.append(list_with_dict[i]['Количество побед'])
                    list_with_col.remove(max(list_with_col))
                    dop['Количество'][list_with_dict[i]['Количество побед']].remove(max(dop['Количество'][list_with_dict[i]['Количество побед']]))
                elif list_with_dict[i]['Количество побед'] not in dop:
                    new_list.append(list_with_dict[i])
                    col_list.append(list_with_dict[i]['Количество побед'])
                    list_with_col.remove(max(list_with_col))
                else:
                    continue
            else:
                continue
        else:
            break

with open('files/results.csv', 'w', newline="", encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Спортсмен', 'Место'])
    for i in range(len(new_list)):
        print(new_list[i])
        writer.writerow([str(new_list[i]['Спортсмен']), str(i + 1)])
