# Welcome to the World of Tomorrow (kinda ez not so much)

### Description

I dont have it sry, read source code insted

### Files

**hash.txt**

> 783f3977627a693a320f313e421e29513e036e485565360a172b00790c211a7b117b4a7814510b2d4b0b01465448580a0369520824294c670c3758706407013e271b624934147f1e70187c1c72666949405c5b4550495e5e02390607217f11695a61587c6351536b741d301d6d182c48254e7f4927683d19

**luggage_combination.py**

> ```python
> from pwn import *
>
> plaintext = b'****************************************'
> key1 = b'****************************************'
> key2 = b'****************************************'
>
> def shield_combination(p, k1, k2):
> 	A = xor(p, k1, k2)
> 	B = xor(p, k1)
> 	C = xor(p, k2)
> 	return A + B + C
>
> print(shield_combination(plaintext, key1, key2).hex())
> ```

### Solution

let's understand the `shield_combination` function to solve it.

`A = xor(p, k1, k2)` means `A = p xor k1 xor k2` - if we xor `A` again with `k2` we get `A xor k1` only, which is `B `... so we can produce that `B = A xor k1` and `C = A xor k2`

```
A = xor(p, k1, k2)

B = xor(A, k2)
C = xor(B, k1)
```

great cuz we know that `A xor k2 xor A = k2` and `A xor k1 xor A = k1` ,We also know that `k2 xor A = C` and `k1 xor A = B,` by substitution we get `A xor B = k1` and `A xor C = k2` so we now have `k1` and `k2` all that is left is to get `P`(plaintext) how? well `A = p xor k1 xor k2` so `A xor k1 and k2 = p`.

how do we get `A`, `B` and `c`?

`plaintext`, `key1` and `key2` lengths are the same 40 chars, i know that when two or more strings of the same length are xored, the output is a string of the same length, so i know that `A`,`B`,`C` are also the same length, so the output can be divided into three equal parts of 40 chars, but the output is printed as hex, so each character is doubled to two characters, so the output is actually split into three 80 characters long parts, lets write a code to do that:

```python
from pwn import *
out = '783f3977627a693a320f313e421e29513e036e485565360a172b00790c211a7b117b4a7814510b2d4b0b01465448580a0369520824294c670c3758706407013e\
271b624934147f1e70187c1c72666949405c5b4550495e5e02390607217f11695a61587c6351536b741d301d6d182c48254e7f4927683d19'

a = unhex(out[:80])
b = unhex(out[80:160])
c = unhex(out[160:])
```

now as explained above lets get `k1` and `k1`

```python
k1 = xor(a, b)
k2 = xor(a, c)
```

from that we can finally get `p`

```python
p = xor(a, k1, k2)
print(p)
```

Full code:

```python
from pwn import *
out = '783f3977627a693a320f313e421e29513e036e485565360a172b00790c211a7b117b4a7814510b2d4b0b01465448580a\
0369520824294c670c3758706407013e271b624934147f1e70187c1c72666949405c5b4550495e5e02390607217f11695a61587c6351536b741d301d6d182c48254e7f4927683d19'

a = unhex(out[:80])
b = unhex(out[80:160])
c = unhex(out[160:])

k1 = xor(a, b)
k2 = xor(a, c)
p = xor(a, k1, k2)
print(p)
```

and if u have big brain energy you can produce that its the same as `a xor b xor c`, or u can just find out accidentally and pretend like me 😄

```python
from pwn import *
out = '783f3977627a693a320f313e421e29513e036e485565360a172b00790c211a7b117b4a7814510b2d4b0b01465448580a\
0369520824294c670c3758706407013e271b624934147f1e70187c1c72666949405c5b4550495e5e02390607217f11695a61587c6351536b741d301d6d182c48254e7f4927683d19'

a = unhex(out[:80])
b = unhex(out[80:160])
c = unhex(out[160:240])

print(xor(b, c, a))
```

Flag ---> shctf{on3_e1GHt_hUnDR3d_D-R-U-I-D-I-A__}

full disclosure, i found the flag by accident and then figured out how it works, i was trying random xors and i got the flag, i was like "wtf"😂
