# [Bynary Encoding](https://spaceheroes.ctfd.io/challenges#Bynary%20Encoding-12) (super ez)

### Description

Starfleet has received a transmission from [Bynaus](https://memory-alpha.fandom.com/wiki/Bynar). However, the message apears to be blank. Is there some kind of hidden message here?

### Files

Transmission.txt

### Solution

when i opened the file it looked empty, until i hit `ctrl+a` then i can see that there are a lot of white spaces, some are single white space and a tap ``\t``.

so using find and replace in ``vscode`` i replaced all `space` with  ``1``and ``\t`` with ``0``.

```python
01110011
01101000
..
..
01110100
01111101
```

now i just wrote a small python script to read these binary nums convert them to decemal and print the coresponding char

```python
with open('transmission.txt','r') as f:
    text = f.readlines()
for i in text:
    c = int(i, 2)  # converts binary to decimal
    c = chr(c)  # converts decimal to ascii
    print(c, end='') # end='' to print in one line
```

shctf{a_bl1nd_m4n_t3aching_an_4ndr0id_h0w_to_pa1nt}
