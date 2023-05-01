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
with open('master.txt', 'w') as f:
    for i in range(0, 8):
        for j in range(0, 163):
            f.write(master[i][j])
        f.write('\n')
    