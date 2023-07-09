## CGaurds (kinda ez)

1237 pts

#### description

This challenge was brought to you by `CGaurds` Note: This challenge works on **python 3.10**

[ challenge.py](./challenge.py)

[ ct.txt](./ct.txt)

### Solution

```python
import marshal
import base64
code=marshal.loads(base64.b64decode("4wAAAAAAAAAAAAAAAAAAAAAFAAAAQAAAAHNgAAAAZABkAWwAWgBlAWQCgwFaAmQDWgNlAkQAXRJaBGUFZQSDAWQEQQBaBmUGZAUXAFoHZQNlCGUHgwE3AFoDcQxlAKAJZQplA2QGgwKhAVoDZQtlA6AMZAahAYMBAQBkAVMAKQfpAAAAAE56EWVudGVyIHRoZSBzYXVjZTog2gBpNxMAAOlBAAAAegV1dGYtOCkN2gZiYXNlNjTaBWlucHV02gRmbGFnWgNlbmPaAWnaA29yZNoFZmlyc3RaBnNlY29uZNoDY2hy2gliNjRlbmNvZGXaBWJ5dGVz2gVwcmludNoGZGVjb2RlqQByDwAAAHIPAAAA+ghjaGFsbC5wedoIPG1vZHVsZT4BAAAAcxIAAAAIAAgCBAIIAgwBCAEOARACEgI="))
exec(code)
```

First we look at the code, we find that it executes a python code that is encoded in base64 and then marshalled. So we need to disassemble it and figure out what it does.

```python
import marshal
import base64
import dis

bytecode = marshal.loads(base64.b64decode("4wAAAAAAAAAAAAAAAAAAAAAFAAAAQAAAAHNgAAAAZABkAWwAWgBlAWQCgwFaAmQDWgNlAkQAXRJaBGUFZQSDAWQEQQBaBmUGZAUXAFoHZQNlCGUHgwE3AFoDcQxlAKAJZQplA2QGgwKhAVoDZQtlA6AMZAahAYMBAQBkAVMAKQfpAAAAAE56EWVudGVyIHRoZSBzYXVjZTog2gBpNxMAAOlBAAAAegV1dGYtOCkN2gZiYXNlNjTaBWlucHV02gRmbGFnWgNlbmPaAWnaA29yZNoFZmlyc3RaBnNlY29uZNoDY2hy2gliNjRlbmNvZGXaBWJ5dGVz2gVwcmludNoGZGVjb2RlqQByDwAAAHIPAAAA+ghjaGFsbC5wedoIPG1vZHVsZT4BAAAAcxIAAAAIAAgCBAIIAgwBCAEOARACEgI="))
dis.dis(bytecode)
```

this prints out some kind if low level code of each step the code takes:

```
1           0 LOAD_CONST               0 (0)
              2 LOAD_CONST               1 (None)
              4 IMPORT_NAME              0 (base64)
              6 STORE_NAME               0 (base64)

  3           8 LOAD_NAME                1 (input)
             10 LOAD_CONST               2 ('enter the sauce: ')
             12 CALL_FUNCTION            1
             14 STORE_NAME               2 (flag)

  5          16 LOAD_CONST               3 ('')
             18 STORE_NAME               3 (enc)

  7          20 LOAD_NAME                2 (flag)
             22 GET_ITER
        >>   24 FOR_ITER                18 (to 62)
             26 STORE_NAME               4 (i)

  8          28 LOAD_NAME                5 (ord)
             30 LOAD_NAME                4 (i)
             32 CALL_FUNCTION            1
             34 LOAD_CONST               4 (4919)
             36 BINARY_XOR
             38 STORE_NAME               6 (first)

  9          40 LOAD_NAME                6 (first)
             42 LOAD_CONST               5 (65)
             44 BINARY_ADD
             46 STORE_NAME               7 (second)

 10          48 LOAD_NAME                3 (enc)
             50 LOAD_NAME                8 (chr)
             52 LOAD_NAME                7 (second)
             54 CALL_FUNCTION            1
             56 INPLACE_ADD
             58 STORE_NAME               3 (enc)
             60 JUMP_ABSOLUTE           12 (to 24)

 12     >>   62 LOAD_NAME                0 (base64)
             64 LOAD_METHOD              9 (b64encode)
             66 LOAD_NAME               10 (bytes)
             68 LOAD_NAME                3 (enc)
             70 LOAD_CONST               6 ('utf-8')
             72 CALL_FUNCTION            2
             74 CALL_METHOD              1
             76 STORE_NAME               3 (enc)

 14          78 LOAD_NAME               11 (print)
             80 LOAD_NAME                3 (enc)
             82 LOAD_METHOD             12 (decode)
             84 LOAD_CONST               6 ('utf-8')
             86 CALL_METHOD              1
             88 CALL_FUNCTION            1
             90 POP_TOP
             92 LOAD_CONST               1 (None)
             94 RETURN_VALUE
```

if ur really smart u can figure out what it does from this, but i am not so i asked chat gpt to turn this madness into python code.

```python
import base64

flag = input('enter the sauce: ')
enc = ''

for i in flag:
    first = ord(i) ^ 4919
    second = first + 65
    enc += chr(second)

enc = base64.b64encode(bytes(enc, 'utf-8')).decode('utf-8')

print(enc.decode('utf-8'))
```

thats what i got

testing the code with some inputs we find that each letter in the string returns a static value, example the letter M always returns `4Y67`. and the letter `C` always returns `4Y6z`, if we input `MC` we get `4Y674Y6z` and so on.

wwe check the key `ct` = `4Y674Y6z` hmmm lets try `METACTF{` = `4Y674Y6z4Y6k4Y634Y614Y6k4Y6Y` which is also the same as our key `ct`

we produce that we can bruteforce on all the letters and find the flag.

```python
import base64
from string import printable

enc_flag=['4Y67' ,'4Y6z' ,'4Y6k' ,'4Y63' ,'4Y61' ,'4Y6k' ,'4Y6Y' ,'4Y6N' ,'4Y6h' ,'4Y6g' ,'4Y2E' ,'4Y6E' ,'4Y6p' ,'4Y2X' ,'4Y6F' ,'4Y6p' ,'4Y6k' ,'4Y6g' ,'4Y2X' ,'4Y2D' ,'4Y6p' ,'4Y6/' ,'4Y6p' ,'4Y6V' ,'4Y2E' ,'4Y6b' ,'4Y2F' ,'4Y6p', '4Y+A' ,'4Y2F' ,'4Y6G' ,'4Y6T' ,'4Y6p' ,'4Y6E' ,'4Y2I' ,'4Y6p' ,'4Y6W' ,'4Y2F' ,'4Y6p' ,'4Y6E' ,'4Y2F' ,'4Y6F' ,'4Y6E' ,'4Y6T' ,'4Y6U' ,'4Y2J' ,'4Y2J' ,'4Y2J' ,'4Y6L']
alpha = printable

for i in enc_flag:
    for j in alpha:
        first = ord(j) ^ 4919
        second = first + 65
        guess = chr(second)
        letter = base64.b64encode(bytes(guess, 'utf-8')).decode('utf-8')
        if letter == i:
            print(j, end='')
            break
```

and that prints the 🏁 METACTF{Wh4t_!s_Th!5_I_c4m3_H3re_t0_b3_t3sted???}
