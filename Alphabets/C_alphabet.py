x=int(input("Enter the number of rows : "))
for i in range(x+1):
    for j in range(x+1):
        if i==0 or i==x or j==0:
            print("*",end='')
        else:
            print("",end='')
    print()