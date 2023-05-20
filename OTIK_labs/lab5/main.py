
#концепт Зива и Лемпеля; ссылка (𝑆, 𝐿) как (𝑆 : 10, 𝐿: 6)
with open("message.txt", "r") as file:
    original_message = file.readlines() #на выходи список сктрок

message_str = ""
for line in original_message: #все строки записываем в одну переменную
    message_str += str(line)

message_list = list(message_str)
result = "00" + message_list[0] # у первого символа не может быть повторений


true = True
skip_character_index = [] #если найдется повтр символов, последующий символ не проходит проверку
for i in range(1, len(message_list)): # перебор символов
    if i in skip_character_index:
        continue
    k = i - 1 # k - индекс элемента, с которым происходит сравнение
    s = 1
    l = 1

    repetition_check = False
    repetition = ""
    end_of_repetitions = -2

    while k >= 0 and s != 10 and (l+1) < 6: #сравнение 1 символа с 6 предыдущими
        if (end_of_repetitions == k): # если цепочка повторных символов кончилась на предыдущей итерации, пропускаем блок
            break

        if(message_list[i] == message_list[k]):
            repetition += message_list[i]
            repetition_check = True
            S = s
            ti = i
            tk = k
            true = True
            skip_character_index.append(ti+1)
            while(true == True): #проверка на повторение последующих символов после нахождения первого повторения
                if ((ti+1) <= len(message_list) - 1) and (message_list[ti+1] == message_list[tk+1]) and (l < 6):
                    repetition += message_list[ti+1]
                    l += 1
                    tk += 1
                    ti += 1
                    skip_character_index.append(ti)
                elif((ti+1) <= len(message_list) - 1) and (message_list[ti+1] != message_list[tk+1]) and (l < 6):
                    true = False
                    end_of_repetitions = k-1
                    skip_character_index.append(ti+1)
                else:
                    true = False
                    end_of_repetitions = k - 1
        k -= 1
        s += 1

    if (repetition_check == True):
        if ti != len(message_list) - 1: #если следующий символ не последний, выводим его
            ti += 1
            result = result + str(S) + str(l) + str(message_list[ti])
        else: #если последний символ
            if ti in skip_character_index: #..входил в цепочку последних повторений, то не выводим его
                result = result + str(S) + str(l)
            else: #..не входил в цепочку последних повторений, то выводим его
                result = result + str(S) + str(l) + str(message_list[ti])
    else: # если не было найдено повторений
        result = result + "00" + str(message_list[i])
        skip_character_index = []


print("\n" + result)
with open("LZResult.txt", "w") as file:
    file.write(result)