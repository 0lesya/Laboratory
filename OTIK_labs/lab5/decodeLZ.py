

with open("LZResult.txt", "r") as file:
   decode_message = file.readlines()

message_str = ""
for line in decode_message: #все строки записываем в одну переменную
    message_str += str(line)

message_list = list(message_str)
result = message_list[2]
i = 3

while (i + 2 <= len(message_list) - 1) or (i + 2 == len(message_list)):
    S = int(message_list[i])
    L = int(message_list[i + 1])
    if (i+2 <= len(message_list) - 1):
        c = message_list[i + 2]
    elif (i+2 == len(message_list)):
        c = ""

    if S == 0: #нет ссылки
        result = result + c
    elif S != 0 and L == 1: #есть односимвольное повторение
        k = len(result) - int(S)
        if i + 3 == len(message_list):
            result = result + result[k]
        else:
            result = result + result[k] + c
    else:  #есть повторение цепочки символов
        while (L)>0:
            k = len(result) - int(S)
            result = result + result[k]
            k+=1
            L-=1
        result += c
    i = i+3

print(result)
