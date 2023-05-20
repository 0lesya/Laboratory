class Decoder:

    def decode(self, cipher, encode_dict):
        decode_information = ""
        encode_dict = {v: k for k, v in encode_dict.items()}
        symbol_cipher = ""
        for i in cipher:
            symbol_cipher += i
            if encode_dict.__contains__(symbol_cipher):
                decode_information += encode_dict[symbol_cipher];
                symbol_cipher = ""
        return decode_information
