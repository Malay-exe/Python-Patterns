def tri(n):
    for i in range(0,n+1):
        for j in range(0,i):
            if i%2==0:
                print("*",end='')
            else:
                print(j,end='')
        print("")
(tri(5))