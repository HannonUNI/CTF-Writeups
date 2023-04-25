# Acheron (ez)

### Description

While researching a foreign planet, you and your team discover a cave with some strange eggs. Upon inspection, something attacked your team. You got separated from them and knocked unconscious. Once awake, you begin running to your ship to regroup with your team. The problem is, you don't remember the way. Find your way back to your ship.

### Files

**Connect**

> ```
> from pwn import *
> p = remote("spaceheroes-acheron.chals.io", 443, ssl=True, sni="spaceheroes-acheron.chals.io")
> p.interactive()
> ```

[Acheron](Acheron)

> ```c
> int32_t main(int32_t argc, char** argv, char** envp)
> puts("                .               …")
> puts("     *   .                  .   …")
> puts("  .         .                   …")
> puts("        o                       …")
> puts("         .              .       …")
> puts("          0     .")
> puts("                 .          .   …")
> puts(" .          \          .        …")
> puts("      .      \   ,")
> puts("   .          o     .           …")
> puts("     .         \                …")
> puts("               #\##\#      .    …")
> puts("             #  #O##\###        …")
> puts("   .        #*#  #\##\###       …")
> puts("        .   ##*#  #\##\##       …")
> puts("      .      ##*#  #o##\#       …")
> puts("          .     *#  #\#     .   …")
> puts("                      \         …")
> puts("____^/\___^--____/\____O________…")
> puts("   /\^   ^  ^    ^              …")
> puts("         --           -         …")
> puts("   --  __                      _…")
> puts(&data_267a)
> puts("You are lost on a hostile alien …")
> char var_28
> fgets(&var_28, 0x1a, stdin)
> if (var_28 != 0x4e)
>     rip()
>     noreturn
> char var_27
> if (var_27 != 0x45)
>     rip()
>     noreturn
> char var_26
> if (var_26 != 0x4e)
>     rip()
>     noreturn
> char var_25
> if (var_25 != 0x57)
>     rip()
>     noreturn
> char var_24
> if (var_24 != 0x53)
>     rip()
>     noreturn
> char var_23
> if (var_23 != 0x53)
>     rip()
>     noreturn
> char var_22
> if (var_22 != 0x45)
>     rip()
>     noreturn
> char var_21
> if (var_21 != 0x57)
>     rip()
>     noreturn
> char var_20
> if (var_20 != 0x53)
>     rip()
>     noreturn
> char var_1f
> if (var_1f != 0x4e)
>     rip()
>     noreturn
> char var_1e
> if (var_1e != 0x45)
>     rip()
>     noreturn
> char var_1d
> if (var_1d != 0x4e)
>     rip()
>     noreturn
> char var_1c
> if (var_1c != 0x53)
>     rip()
>     noreturn
> char var_1b
> if (var_1b != 0x53)
>     rip()
>     noreturn
> char var_1a
> if (var_1a != 0x57)
>     rip()
>     noreturn
> char var_19
> if (var_19 != 0x45)
>     rip()
>     noreturn
> char var_18
> if (var_18 != 0x45)
>     rip()
>     noreturn
> char var_17
> if (var_17 != 0x4e)
>     rip()
>     noreturn
> char var_16
> if (var_16 != 0x57)
>     rip()
>     noreturn
> char var_15
> if (var_15 != 0x53)
>     rip()
>     noreturn
> char var_14
> if (var_14 != 0x4e)
>     rip()
>     noreturn
> char var_13
> if (var_13 != 0x4e)
>     rip()
>     noreturn
> char var_12
> if (var_12 != 0x45)
>     rip()
>     noreturn
> char var_11
> if (var_11 != 0x53)
>     rip()
>     noreturn
> char var_10
> if (var_10 == 0x53)
>     success()
> return 0
> ```

### Solution

When i downloaded **Acheron** i opened it with **Binary Ninja** **Cloud** and found the code up there, i copied it into vscode and started my [find and replace](solve.txt).

* 0x4e -> N
* 0x45 -> E
* 0x57 -> W
* 0x53 -> S

then i went over them one by one and i got the String `NENWSSEWSNENSSWEENWSNNESS` and i just sent that.

[solve.py](solve.py)

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
> [*] Got EOF while reading in interactive
