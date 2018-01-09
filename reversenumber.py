# 3)To enter a number and find the reverse of that number

num=input(" Enter a number = \n")
temp=num
reverse=0

while (num>0):
    x=num%10
    reverse=reverse*10+x
    num=num/10

print " Reverse of %d is : %d " %(temp,reverse)

