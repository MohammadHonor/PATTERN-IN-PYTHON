# taking multiple input


# using split()


x,y = input("Enter two values:").split(',')

#taking input at time

print("first number is {} and second number is {}".format(x,y))


# using map() with split

num1,num2=map(int,input("Enter a two number by comma seperated").split(","))

print("first number is {} and second number is {}".format(num1,num2))

# using list comprehension

num1,num2=[int(x) for x in input("Enter a two number by comma seperated").split(",")]

print("first number is {} and second number is {}".format(num1,num2))

