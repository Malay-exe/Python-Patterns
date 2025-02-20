x = 7
for i in range(x):
    for j in range(x):
        if j == 0 or (i==0 and j<x-1) or (i==x//2 and j <x-1) or (i==x-1 and j<x-1) or (j==x-1 and (i>0 and i<x//2 or i>x//2 and i<x-1)):
            print("*", end='')
        else:
            print(" ", end='')
    print()
