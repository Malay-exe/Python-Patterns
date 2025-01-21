def tri(n):
    for loop in range(n+1):
        print(' ' * (n - loop - 1), end='')
        for i in range(loop+1):
            print(i,end='')
        for j in range(loop):
            print(chr(65+j),end='')
        print()         
n=4
tri(n)