def tri(n):
    eve=2
    for i in range(0,n+1):
        for j in range(i):
            print(eve,end=' ')
            eve+=2
        print()    
(tri(5))