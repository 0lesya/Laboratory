import os

filename = 'files/article_rus.txt'
# new_file = open(filename, 'w', encoding='utf-8')
# old_file = open('files/book.txt', 'r')
# while os.path.getsize(filename) <= 10240:
#   for lines in old_file:
#          new_file.write(lines)
# old_file.close()
# new_file.close()
count_dict = dict()
file = open(filename, 'r', encoding='utf-8')
sum_alf = 0
for i in range(ord('а'), ord('а') + 32):
    count_dict[chr(i)] = 0
lines = file.readlines()

for j in range(len(lines)):
    for i in range(ord('а'), ord('а') + 32):
        coun = lines[j].count(chr(i)) + lines[j].count((chr(i).lower()))
        count_dict[chr(i)] += coun
        sum_alf += coun

for key in count_dict.keys():
    value = count_dict[key] / sum_alf
    count_dict[key] = value

sorted_values = sorted(count_dict.values(), reverse=True)

new_sorted_dictionary = {}

for i in sorted_values:
    for k in count_dict.keys():
        if count_dict[k] == i:
            new_sorted_dictionary[k] = count_dict[k]
            break

with open('files/article_rus_solve.txt', 'w', encoding='utf-8') as new_file:
    for key in new_sorted_dictionary.keys():
        new_file.write(str(key) + ': ' + str(new_sorted_dictionary[key]) + '\n')
