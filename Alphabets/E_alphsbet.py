x=5
for i in range(x):
    for j in range(x):
        if i==0 or i==x-1 or j==0 or i==x//2:
            print("*", end='')
        else:
            print(" ", end='')
    print()