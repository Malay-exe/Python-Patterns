x=int(input("Enter the number of rows : "))
for i in range(x):
    for j in range(x):
        if i==0 or i==x-1 or j==x-i-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()