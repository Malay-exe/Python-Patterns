def tri(n):
    for i in range(0,n+1):
        for j in range(0,i):#or you can use only 'i' in the j condition
            print("*",end='')
        print("")
(tri(5))