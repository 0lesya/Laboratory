from operator import itemgetter
from shannon.Decoder import Decoder
from shannon.Shannon_fano import Shannon_fano


class Encoder:
    def __init__(self):
        self.encode_dict = {}

    algorithm = Shannon_fano()

    def __del__(self):
        encode_dict = {}
        return encode_dict

    def encrypt(self, information):
        self.__do_encrypt_algorithm(information)
        return self.__write_encrypt(information)

    def __do_encrypt_algorithm(self, information):
        probabilities_dict = self.__create_probabilities_dict(information)
        symbols = list(probabilities_dict.keys())
        weights = list(probabilities_dict.values())
        self.algorithm.encript(weights, "")
        self.__create_encode_dictionary(symbols)

    def __create_probabilities_dict(self, information):
        d = {}
        for s in information:
            if d.__contains__(s) == False:
                d[s] = 1
            else:
                d[s] += 1
        return dict(sorted(d.items(), reverse=True, key=itemgetter(1)))

    def __create_encode_dictionary(self, symbols):
        for i in range(len(symbols)):
            self.encode_dict[symbols[i]] = self.algorithm.encode_list[i]
        return self.encode_dict

    def __write_encrypt(self, information):
        chifer = ""
        for byte in information:
            chifer += self.encode_dict[byte]
        return chifer


#coder = Encoder()
#cipher = coder.encrypt("Небо нло зелено")
#coder1 = Encoder()

#fdf = coder1.encrypt('лучший на свете хых')
#decoder = Decoder()
#decoder1 = Decoder()
#information = decoder.decode(cipher, coder.encode_dict)
#print(coder.encode_dict)
#information1 = decoder1.decode(fdf, coder1.encode_dict)
#print(coder1.encode_dict)
#print(information)
#print(information1)
