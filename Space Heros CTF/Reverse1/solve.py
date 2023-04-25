from pwn import *
p = remote("spaceheroes-acheron.chals.io", 443, ssl=True, sni="spaceheroes-acheron.chals.io")
p.send('NENWSSEWSNENSSWEENWSNNESS')
p.interactive()

