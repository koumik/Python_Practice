# 5)To enter a number and Armstrong Number or Not.

num=input("Enter a Number = \n")
sum=0
temp=num

while temp>0:
    d=temp%10
    sum=sum+d**3
    temp=temp/10

if (num==sum):
    print "Armstrong Number"
else:
    print "Not Armstrong Number"

