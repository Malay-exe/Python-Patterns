def tri(n):
    odd=1
    for i in range(0,n+1):
        for j in range(i):
            print(odd,end=' ')
            odd+=2
        print()    
(tri(5))