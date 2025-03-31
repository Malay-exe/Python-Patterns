x=7
for i in range(x):
    for  j in range(x):
        if i==0 or j==0 or i==x//2 or (j==x-1 and i<=x//2) or (i>=x//2 and i==j+1):
            print("*",end='')
        else:
            print(" ",end='')
    print()
