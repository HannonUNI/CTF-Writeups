from itertools import permutations
from Crypto.Util.number import long_to_bytes

e = 65537
n = 4629059450272139917534568159172903078573041591191268130667
c = 6743459147531103219359362407406880068975344190794689965016
p = 62682123970325402653307817299
q = 73849754237166590568543300233

phi = (p-1)*(q-1)
d = pow(e, -1, phi)

perm = range(10)
permutations_list = list(permutations(perm))

for i in permutations_list:
    flag = ''.join([str(i.index(int(x))) for x in str(c)])
    flag = long_to_bytes(pow(int(flag), d, n))
    if b'ctf{' in flag:
        print(f'flag = {flag}')
        break

# flag = b'ctf{cryptpainfulflag}'
