# hollow triaggle

n=int(input("Enter row:"))
for i in range(1,n+1):
    for j in range(1,n*2):
        if i+j==n+1 or j-i==n-1 or i==n:
            print("*",end="")
        else:
            print(" ",end="")
    print()        



