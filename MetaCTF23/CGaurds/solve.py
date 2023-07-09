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

