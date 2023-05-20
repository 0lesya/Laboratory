with open('key.txt', 'r') as key_file:
    key = key_file.readline()

with open('file2.txt', 'r', encoding='utf-8') as file:
    code_line = ''.join(file.readlines())


def writing_rows_to_table(line, size):
    matrix = []
    while line:
        matrix.append(list(line[:size]))
        line = line[size:]
    while len(matrix[-1]) != size:
        matrix[-1] += 'z'
    return matrix


column_dic = dict()

for i in range(len(key)):
    ans = ''
    for row in writing_rows_to_table(code_line, 5):
        ans += row[int(i)]
    column_dic[key[i]] = ans

sorted_column = dict(sorted(column_dic.items()))

answer = ''
for k in sorted_column.keys():
    answer += sorted_column[k]

print(answer)
print('----------------------')


decode_line = answer
ans_list = []

for i in key:
    ans_list.append(writing_rows_to_table(decode_line, len(decode_line)//5)[int(i)-1])

decode_answer = ''
for i in range(len(decode_line)//5):
    for row in ans_list:
        decode_answer += row[i]
print(decode_answer)
