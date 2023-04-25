with open('./crypto 1 binary/transmission fixed.txt','r') as f:
    text = f.readlines()


for i in text:
    print(chr(int(i, 2)), end='')