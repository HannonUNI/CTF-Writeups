with open('mores.txt','r') as f:
    text = f.readlines()

for i in text:
    print(chr(int(i, 2)), end='')