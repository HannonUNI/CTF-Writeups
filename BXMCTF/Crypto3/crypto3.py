
from Crypto.Util.number import *
import random

e = 65537
n = 4629059450272139917534568159172903078573041591191268130667
c = 6743459147531103219359362407406880068975344190794689965016

p = getPrime(96)
q = getPrime(96)
n = p*q
e = 65537

flag = b'ctf{0000000000000000}'
flag = str(pow(bytes_to_long(flag), e, n))

perm = list(range(10))
random.shuffle(perm)
perm = list(map(str, perm))

c = ''.join([perm[int(x)] for x in flag])

print(f'e = {e}')
print(f'n = {n}')
print(f'c = {c}')
