number=7
spisok=[1,2,3,4,5,6]
while True:
    count = 0
    answer = []
    for i in spisok:
        count += i
        answer.append(i)
        if count == number:
            print(answer)
            break
        elif count > number:
            spisok = spisok[1:]
            answer = []
    
