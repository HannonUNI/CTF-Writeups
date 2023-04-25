# Battleboats In Space

### Description

I love playing this game of battleship, but there's always this `Flag: 1` at the start and I don't get why... Can you help us make the right map for our game?

Run with `./battleship NUMBER_SHOTS MAP_FILE` where NUMBER_SHOTS is an integer and MAP_FILE is a .txt file. The provided mapfile has the number of rows and columns seperated by a space at the top and the map below it. The example can be run with `./battleship 200 example_map.txt`.

Good luck blasting!

### Files

[battleship.c](./battleship.c)

### Solution

Itried the game for a while, won a couple of times, then realized thats its pointless, then i figuered i make my own map and based on the code provided, after some regex replacing i wrote this script:

[solve.py](solve.py)

```python
master = [['~' for i in range(163)] for j in range(9)]
master[1][2] = 'B'
master[1][3] = 'B'
master[1][4] = 'B'
master[1][5] = 'B'
master[1][6] = 'B'
master[1][9] = 'B'
master[1][16] = 'B'
master[1][19] = 'B'
master[1][20] = 'B'
master[1][21] = 'B'
master[1][22] = 'B'
master[1][23] = 'B'
# .
# .
# .
# .
# .
master[7][148] = 'B'
master[7][149] = 'B'
master[7][151] = 'B'
master[7][159] = 'B'
# print("master = ", master)
with open('flag.txt', 'w') as f:
    for i in range(0, 8):
        for j in range(0, 163):
            f.write(master[i][j])
        f.write('\n')
  
```

And it prints the flag directly as art:

[flag.txt](flag.txt)

```
~~BBBBB~~B~~~~~~B~~BBBBB~~BBBBBBB~BBBBBBB~~~~B~~BBBBB~~BBBBBBB~B~~~~~B~B~~~~B~~~~~~~~~BBBBBBB~B~~~~~~B~~~~B~~~BBBBBBB~~~~~~~~~~BBBBB~~B~~~~~~B~BBBBBBB~BBBBBB~~B~~~
~B~~~~~B~B~~~~~~B~B~~~~~B~~~~B~~~~B~~~~~~~~~B~~B~~~~~B~~~~B~~~~BB~~~~B~B~~~B~~~~~~~~~~~~~B~~~~B~~~~~~B~~~B~B~~~~~B~~~~~~~~~~~~B~~~~~B~B~~~~~~B~~~~B~~~~B~~~~~B~~B~~
~~~~~~~~~B~~~~~~B~B~~~~~~~~~~B~~~~BBBBB~~~~B~~~B~~~~~~~~~~B~~~~B~B~~~B~B~~B~~~~~~~~~~~~~~B~~~~B~~~~~~B~~~B~B~~~~~B~~~~~~~~~~~~B~~~~~~~B~~~~~~B~~~~B~~~~B~~~~~B~~~B~
~~BBBBB~~BBBBBBBB~B~~~~~~~~~~B~~~~B~~~~~~~B~~~~~BBBBB~~~~~B~~~~B~~B~~B~BB~~~~~~~~~~~~~~~~B~~~~BBBBBBBB~~BBBBB~~~~B~~~~~~~~~~~~~BBBBB~~BBBBBBBB~~~~B~~~~BBBBBB~~~~~B
~~~~~~~B~B~~~~~~B~B~~~~~~~~~~B~~~~B~~~~~~~~B~~~~~~~~~B~~~~B~~~~B~~~B~B~B~~B~~~~~~~~~~~~~~B~~~~B~~~~~~B~~B~~~B~~~~B~~~~~~~~~~~~~~~~~~B~B~~~~~~B~~~~B~~~~B~~~~~~~~~B~
~B~~~~~B~B~~~~~~B~B~~~~~B~~~~B~~~~B~~~~~~~~~B~~B~~~~~B~~~~B~~~~B~~~~BB~B~~~B~~~~~~~~~~~~~B~~~~B~~~~~~B~~B~~~B~~~~B~~~~~~~~~~~~B~~~~~B~B~~~~~~B~~~~B~~~~B~~~~~~~~B~~
~~BBBBB~~B~~~~~~B~~BBBBB~~~~~B~~~~B~~~~~~~~~~B~~BBBBB~~BBBBBBB~B~~~~~B~B~~~~B~BBBBBBB~~~~B~~~~B~~~~~~B~~B~~~B~~~~B~~~~BBBBBBB~~BBBBB~~B~~~~~~B~BBBBBBB~B~~~~~~~B~~~
```

Flag ---> SHCTF{SINK_THAT_SHIP}
