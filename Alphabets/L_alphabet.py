x=7
for i in range(x):
    for j in range(x):
        if j==0 or i==x-1:
            print("*", end='')
        else:
            print(" ", end='')
    print()

