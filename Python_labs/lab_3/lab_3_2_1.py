def F(n: int) -> int:
    if n == 0:
        f = 1
    else:
        f = n - M(F(n-1))
    return f


def M(n: int) -> int:
    if n == 0:
        m = 0
    else:
        m = n - F(M(n-1))
    return m


def hofstadter_f_m(n: int) -> list:
    list_f_m = [(F(i), M(i)) for i in range(n)]
    yield list_f_m


for j in hofstadter_f_m(5):
    print(j)


