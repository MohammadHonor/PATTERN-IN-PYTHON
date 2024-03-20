row = int(input("Enter Number of row"))
temp=row+1
for i in range(row,0,-1):
    print(" "*i,"*"*(temp-i),end="")
    print("*"*(row-i),end="\n")
    


