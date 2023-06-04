# RAID Safety Assays, But Fixed (kinda ez)

#### Description

Author: cg

The flag to this challenge is all lowercase, with no underscores.-
---
#### Files

[Crypto3.py](./crypto3.py)

```

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
```
---
#### Solution

First Step was finding `p` and `q` in order to find `d` i checked [factordp.com](http://factordb.com/index.php?query=4629059450272139917534568159172903078573041591191268130667) (it'll be factorized there by now) but at the time it wasn't so i head to [alpertron.com](https://www.alpertron.com.ar/ECM.HTM) and used there factoring method to find `p` and `q` now we can calculate `phi` and `d`

```python
e = 65537
n = 4629059450272139917534568159172903078573041591191268130667
c = 6743459147531103219359362407406880068975344190794689965016
p = 62682123970325402653307817299
q = 73849754237166590568543300233

phi = (p-1)*(q-1)
d = pow(e, -1, phi)
```

i see that `c` was not released straight forward:

```python
perm = list(range(10))
random.shuffle(perm)
perm = list(map(str, perm))

c = ''.join([perm[int(x)] for x in flag])
```

but rather shuffled based on a `perm` list so i had to find the write permutation in order to find the real `c`, but there is no way to find what `perm` really is, so there are two ways to about  this:

1- find all possible permutations for numbers from 0 to 9, and rearrange `c` based on them (doable and feasible)
2- shuffle `c` randomly just like `perm` was and test my luck (stupid and guessy)

i know that iam dump and lucky so i wend with way two 😄

[Full code](solve.py)

```python
while True:
    perm = list(range(10))
    random.shuffle(perm) #shuffle a list of 0-9
    flag = ''.join([str(perm.index(int(x))) for x in str(c)]) # map each index in flag to perm
    flag = long_to_bytes(pow(int(flag), d, n))
    if b'ctf{' in flag:
        print(f'flag = {flag}')
```

after 2~3 minutes i got the flag:

***flag = b'ctf{cryptpainfulflag}'***
