from pwn import *

chars = 'abcdefghijklmnopqrstuvwxyz0123456789_{}ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()+|'
flag = 'shctf'
last_count = 0
letter = '{'
while True:
    p = remote("spaceheroes-cryptographic-space-rover.chals.io", 443,
               ssl=True, sni="spaceheroes-cryptographic-space-rover.chals.io")
    r = str(p.recvuntil("Please enter characters:: "))
    uuid = r.split("Session UUID:")[1][58:58+37].strip()
    
    guess = flag+letter
    print(guess)
    p.sendline(guess.encode())

    all = p.recvall()
    counter = all.count(uuid.encode())
    if counter > last_count:
        flag += letter
        if letter == '}':
            print(f'{flag = }')
            break
        last_count = counter
        letter = chars[0]
        guess = flag+letter
        continue
    else:
        p.close()
        letter = chars[chars.find(letter)+1]
        guess = flag+letter
        continue

# shctf{met30rs_4r3nt_as_b4d_4s_sl0w_cpu}