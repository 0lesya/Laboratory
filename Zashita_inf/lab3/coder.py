import sys

BMP_HEADER_SIZE = 54


def encode_image(input_img_name, output_img_name, txt_file, degree):

    text = open(txt_file, 'r')
    input_image = open(input_img_name, 'rb')
    output_image = open(output_img_name, 'wb')

    bmp_header = input_image.read(BMP_HEADER_SIZE)
    output_image.write(bmp_header)

    text_mask, img_mask = 0b11000000, 0b11111100

    while True:
        symbol = text.read(1)
        if not symbol:
            break
        symbol = ord(symbol)

        for _ in range(0, 8, degree):
            img_byte = int.from_bytes(input_image.read(1), sys.byteorder) & img_mask
            bits = symbol & text_mask
            bits >>= (8 - degree)
            img_byte |= bits

            output_image.write(img_byte.to_bytes(1, sys.byteorder))
            symbol <<= degree

    output_image.write(input_image.read())

    text.close()
    input_image.close()
    output_image.close()

    return True


def decode_image_with_no_size(encoded_img, output_txt, degree):
    text = open(output_txt, 'wb')
    encoded_bmp = open(encoded_img, 'rb')
    encoded_bmp.seek(BMP_HEADER_SIZE)

    img_mask = ~0b11111100
    while True:
        symbol = 0
        for bits_read in range(0, 8, degree):
            byte = encoded_bmp.read(1)
            if byte == b'\xff':
                break
            else:
                img_byte = int.from_bytes(byte, sys.byteorder) & img_mask
                symbol <<= degree
                symbol |= img_byte

        try:
            text.write(symbol)
        except:
            break

    text.close()
    encoded_bmp.close()
    return True


def decode_image_with_size(encoded_img, output_txt, size,  degree):
    text = open(output_txt, 'wb')
    encoded_bmp = open(encoded_img, 'rb')
    encoded_bmp.seek(BMP_HEADER_SIZE)

    img_mask = ~0b11111100
    read=0
    while read<size:
        symbol = 0
        for bits_read in range(0, 8, degree):
            byte = encoded_bmp.read(1)
            img_byte = int.from_bytes(byte, sys.byteorder) & img_mask
            symbol <<= degree
            symbol |= img_byte
        read += 1
        try:
            text.write(symbol)
        except:
            break
    text.close()
    encoded_bmp.close()
    return True


encode_image("input_img.bmp", "output_img_encode.bmp", "text.txt", 2)
decode_image_with_no_size("2.bmp", "out_text.txt", 2)
decode_image_with_no_size("output_img_encode.bmp", "out_text_test.txt", 2)
decode_image_with_size("output_img_encode.bmp", "out_text_test_size.txt", 47, 2)
decode_image_with_size("2.bmp", "out_text_size.txt", 30, 2)
