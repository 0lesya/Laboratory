import math


def reducer(n: int, m: int) -> tuple:
    try:
        k = math.gcd(n, m) #возвращает наибольший общий делитель
        if m == 0:
            return 'Попытка деления числа на нуль'
        else:
            return (n//k, m//k)
    except Exception:
        return 'Данные введены неверно. Попробуйте еще раз с правильной дробью'


print(reducer(3, 5))
print(reducer(2, 4))
print(reducer('d', 10))
print(reducer(2, 10))
print(reducer(2, 0))


