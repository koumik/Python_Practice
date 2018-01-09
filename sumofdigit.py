# 2)To enter a number and find the sum of digit of that number

num=input(" Enter the number = ")
sum=0
temp=num

while (num>0):
    d=num%10
    sum=sum+d
    num=num/10

print "Sum of %d is = %d "%(temp,sum)
