# 6)To enter a number and check this number is Palindrome or Not.

num=input(" Enter a number = \n")
temp=num
reverse=0

while (num>0):
    x=num%10
    reverse=reverse*10+x
    num=num/10

if (temp==reverse):
    print "Number is Palindrome"
else:
    print "Number is not Palindrome"
