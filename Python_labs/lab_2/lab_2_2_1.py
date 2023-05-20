def comp_to_int(line):
    line = [int(i) for i in line.split('.')]
    return line


def get_address(ip_p, mask_p):
    answer = []
    for i in range(4):
        answer.append(str(int(bin(ip_p[i] & mask_p[i])[2:], 2)))

    return '.'.join(answer)


mask = comp_to_int(input() + '.' + input() + '.' + input() + '.' + input())

file_address = open('files/ip_solve.log', 'w')

with open('files/ip.log', 'r') as ip_file:
    ip_array = ip_file.readlines()
    for ip in ip_array:
        ip = comp_to_int(ip)
        file_address.write(get_address(ip, mask) + '\n')

ip_file.close()

test_ip = '192.168.1.2'
test_mask = '255.255.254.0'
test_ip = comp_to_int(test_ip)
test_mask = comp_to_int(test_mask)
print(get_address(test_ip, test_mask))
