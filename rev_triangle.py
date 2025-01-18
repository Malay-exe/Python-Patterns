def tri(n):
    for i in range(n):
        for j in range(n-i):
            print('*',end='')
        print()    
(tri(5))