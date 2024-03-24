n=int(input('Enter number of rows'))
for row in range(1,n+1):
    for col in range(1,n*2):
        if row+col==row*2 or row+col==n*2 or row==1:
            print("*",end="")
        else:
            print(end=" ")
    print()        