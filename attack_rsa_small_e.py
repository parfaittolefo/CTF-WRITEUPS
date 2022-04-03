from Crypto.Util.number import inverse, long_to_bytes
from sympy import integer_nthroot


file = open("output.txt", "rb")

while True:
    n = int(file.readline().strip())
    c = int(file.readline().strip())
    dis = file.readline()
    while True:
        ans = integer_nthroot(c, 4)
        if ans[1]:
            m = ans[0]
            break

    plaintext = long_to_bytes(m).decode()
    print(plaintext)
