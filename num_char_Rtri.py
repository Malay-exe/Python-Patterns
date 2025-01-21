def tri(n):
    for loop in range(n+1):
        for i in range(loop+1):
            print(i,end='')
        for j in range(i+1):
            print(chr(65+j),end='')
        print()
n=4
tri(n)