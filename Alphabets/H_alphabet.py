x=9
for i in range(x):
    for j in range(x):
        if j==0 or j==x-1 or i==x//2:
            print("*", end='')
        else:
            print(" ", end='')
    print()