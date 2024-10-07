import math

a = int(input())
if a < 0:
    bits = math.floor(math.log(abs(a), 2))+2
    a = (1 << bits) - abs(a)
k = 0
while a != 0:
    k += a & 1
    a >>= 1
print(k)
