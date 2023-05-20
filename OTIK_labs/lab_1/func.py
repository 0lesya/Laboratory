def amount_lines(filename):
    file = open(filename, 'r', encoding='utf-8')
    return len(file.readlines())
