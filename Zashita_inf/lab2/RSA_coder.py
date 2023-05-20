import math


class Coder:
    def __init__(self, p, q):
        self.p, self.q = p, q
        self.n = self.p*self.q
        self.eler_func = (self.p-1)*(self.q-1)
        self.open_key = (self.find_e(), self.n)
        self.close_key = (self.find_d(), self.n)

    def find_e(self):
        e = 1
        for i in range(2, self.n):
            if math.gcd(self.eler_func, i) == 1:
                e = i
                break
        return e

    def find_d(self):
        k = 1
        d = ((k * self.eler_func) + 1) / self.open_key[0]
        while int(d) != float(d):
            k += 1
            d = ((k * self.eler_func) + 1) / self.open_key[0]
        return int(d)

    def encode(self, line):
        coder_line = []
        for letter in line:
            coder_line.append(pow(filling_dict_alfabet()[letter], self.open_key[0]) % self.n)
        return coder_line

    def decode(self, line):
        decoder_line = ''
        for num in line:
            decoder = pow(num, self.close_key[0]) % self.n
            for key, value in filling_dict_alfabet().items():
                if value == decoder:
                    decoder_line += key
        return decoder_line


def filling_dict_alfabet():
    alfabet, count = dict(), 1
    for i in range(ord('А'), ord('Я')+1):
        alfabet[chr(i)] = count
        count += 1
    alfabet[' '] = count
    count += 1
    for i in range(0, 10):
        alfabet[str(i)] = count
        count += 1
    return alfabet


code_line = 'какой то небольшой текст для проверки работы кодера и декодера'.upper()
coder = Coder(6, 73)
encode_answer = coder.encode(code_line)
print(encode_answer)
print(coder.decode(encode_answer))
