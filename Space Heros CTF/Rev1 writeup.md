# Acheron (ez)

### Description

While researching a foreign planet, you and your team discover a cave with some strange eggs. Upon inspection, something attacked your team. You got separated from them and knocked unconscious. Once awake, you begin running to your ship to regroup with your team. The problem is, you don't remember the way. Find your way back to your ship.

### Files

**Connect.py**

> ```
> from pwn import *
> p = remote("spaceheroes-acheron.chals.io", 443, ssl=True, sni="spaceheroes-acheron.chals.io")
> p.interactive()
> ```

**Acheron**

> ```python
> int32_t main(int32_t argc, char** argv, char** envp)
> 000011bd  puts("                .               …")
> 000011cc  puts("     *   .                  .   …")
> 000011db  puts("  .         .                   …")
> 000011ea  puts("        o                       …")
> 000011f9  puts("         .              .       …")
> 00001208  puts("          0     .")
> 00001217  puts("                 .          .   …")
> 00001226  puts(" .          \          .        …")
> 00001235  puts("      .      \   ,")
> 00001244  puts("   .          o     .           …")
> 00001253  puts("     .         \                …")
> 00001262  puts("               #\##\#      .    …")
> 00001271  puts("             #  #O##\###        …")
> 00001280  puts("   .        #*#  #\##\###       …")
> 0000128f  puts("        .   ##*#  #\##\##       …")
> 0000129e  puts("      .      ##*#  #o##\#       …")
> 000012ad  puts("          .     *#  #\#     .   …")
> 000012bc  puts("                      \         …")
> 000012cb  puts("____^/\___^--____/\____O________…")
> 000012da  puts("   /\^   ^  ^    ^              …")
> 000012e9  puts("         --           -         …")
> 000012f8  puts("   --  __                      _…")
> 00001307  puts(&data_267a)
> 00001316  puts("You are lost on a hostile alien …")
> 0000132e  char var_28
> 0000132e  fgets(&var_28, 0x1a, stdin)
> 00001339  if (var_28 != 0x4e)
> 00001340      rip()
> 00001340      noreturn
> 00001350  char var_27
> 00001350  if (var_27 != 0x45)
> 00001357      rip()
> 00001357      noreturn
> 00001367  char var_26
> 00001367  if (var_26 != 0x4e)
> 0000136e      rip()
> 0000136e      noreturn
> 0000137e  char var_25
> 0000137e  if (var_25 != 0x57)
> 00001385      rip()
> 00001385      noreturn
> 00001395  char var_24
> 00001395  if (var_24 != 0x53)
> 0000139c      rip()
> 0000139c      noreturn
> 000013ac  char var_23
> 000013ac  if (var_23 != 0x53)
> 000013b3      rip()
> 000013b3      noreturn
> 000013c3  char var_22
> 000013c3  if (var_22 != 0x45)
> 000013ca      rip()
> 000013ca      noreturn
> 000013da  char var_21
> 000013da  if (var_21 != 0x57)
> 000013e1      rip()
> 000013e1      noreturn
> 000013f1  char var_20
> 000013f1  if (var_20 != 0x53)
> 000013f8      rip()
> 000013f8      noreturn
> 00001408  char var_1f
> 00001408  if (var_1f != 0x4e)
> 0000140f      rip()
> 0000140f      noreturn
> 0000141f  char var_1e
> 0000141f  if (var_1e != 0x45)
> 00001426      rip()
> 00001426      noreturn
> 00001436  char var_1d
> 00001436  if (var_1d != 0x4e)
> 0000143d      rip()
> 0000143d      noreturn
> 0000144d  char var_1c
> 0000144d  if (var_1c != 0x53)
> 00001454      rip()
> 00001454      noreturn
> 00001464  char var_1b
> 00001464  if (var_1b != 0x53)
> 0000146b      rip()
> 0000146b      noreturn
> 0000147b  char var_1a
> 0000147b  if (var_1a != 0x57)
> 00001482      rip()
> 00001482      noreturn
> 00001492  char var_19
> 00001492  if (var_19 != 0x45)
> 00001499      rip()
> 00001499      noreturn
> 000014a9  char var_18
> 000014a9  if (var_18 != 0x45)
> 000014b0      rip()
> 000014b0      noreturn
> 000014c0  char var_17
> 000014c0  if (var_17 != 0x4e)
> 000014c7      rip()
> 000014c7      noreturn
> 000014d7  char var_16
> 000014d7  if (var_16 != 0x57)
> 000014de      rip()
> 000014de      noreturn
> 000014eb  char var_15
> 000014eb  if (var_15 != 0x53)
> 000014f2      rip()
> 000014f2      noreturn
> 000014ff  char var_14
> 000014ff  if (var_14 != 0x4e)
> 00001506      rip()
> 00001506      noreturn
> 00001513  char var_13
> 00001513  if (var_13 != 0x4e)
> 0000151a      rip()
> 0000151a      noreturn
> 00001527  char var_12
> 00001527  if (var_12 != 0x45)
> 0000152e      rip()
> 0000152e      noreturn
> 0000153b  char var_11
> 0000153b  if (var_11 != 0x53)
> 00001542      rip()
> 00001542      noreturn
> 0000154f  char var_10
> 0000154f  if (var_10 == 0x53)
> 00001556      success()
> 00001561  return 0
> ```
>

### Solution

When i downloaded **Acheron** i opened it with **Binary Ninja** **Cloud** and found the code up there, i copied it into vscode and started my find and replace.

* 0x4e -> N
* 0x45 -> E
* 0x57 -> W
* 0x53 -> S

then i went over them one by one and i got the String `NENWSSEWSNENSSWEENWSNNESS` and i just sent that.

```python
from pwn import *
p = remote("spaceheroes-acheron.chals.io", 443, ssl=True, sni="spaceheroes-acheron.chals.io")
p.send('NENWSSEWSNENSSWEENWSNNESS')
p.interactive()
```

And thats the output:

> You are lost on a hostile alien planet. You gotta navigate your way back to your ship! (Acceptable input is N, S, E, W):
> You made it back to your ship successfully, you feel a weird sensation in your chest however...
> shctf{gam3_0v3r_m@n_game_0ver}.
>
> [*] Got EOF while reading in interactive
