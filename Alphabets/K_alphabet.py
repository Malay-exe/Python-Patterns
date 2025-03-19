x=7
for i in range(x):
    for j in range(x):
        if j==0 or (j==x-i-2 and i<=x//2)or(i>=x//2 and j==i-1):
            print("*", end='')
        else:
            print(" ", end='')
    print()

