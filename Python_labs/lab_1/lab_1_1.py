s, x = input(), input()
while x.lower() in s.lower():
    s = s.replace(x.lower(), '')
print(s)
