# 1) To find max of three numbers.

x=input("Enter 1st Number :")
y=input("Enter 2nd Number :")
z=input("Enter 3rd Number :")

if (x>= y) and (x >=z):
   largest = x
elif (y>= x) and (y >=z):
   largest = y
else:
   largest = z

print("The largest number between",x,",",y,"and",z,"is",largest)
