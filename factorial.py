# 4)To enter a number and find the factorial of that number

num=input("Enter the Number : \n")
f=1
if num<0:
    print "Not applicable"
elif num==0:
    print " Factorial is 1 "
else:
    for i in range(1,num+1):
        f=f*i
    print "The factorial of %d is : %d" %(num,f)

