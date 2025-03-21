x=7
for i in range(x):
    for j in range(x):
        if j==0 or (j==i and i<=x//2) or (j==x-i-1 and i<=x//2) or j==x-1:
            print("*", end='')
        else:
            print(" ", end='')
    print()

