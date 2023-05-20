import os
from random import randint
if not os.path.isdir("example"):
    os.mkdir("example")
os.chdir("example")
for i in range(100):
    f = open("file_{}".format(i+1), "wb")
    size = randint(1024, 102400)
    f.write("\0".encode() * size)
    f.close()
    