x=9
for i in range(x):
    for j in range(x):
        if i==0 or j==0 or i==x-1 or (j==x-1 and i>=x//2 ) or (i==x//2 and j>x//2):
            print("*", end='')
        else:
            print(" ", end='')
    print()
# another G
x = 9
for i in range(x):
    for j in range(x):
        if ((j == 0 or (i == 0 and j != 0) or i == x - 1 or (j == x - 1 and i >= x // 2) or (i == x // 2 and j > x // 2)) and not (i == 0 and j == 0)) and not (i == x - 1 and j == 0):
            print("*", end='')
        else:
            print(" ", end='')
    print()
