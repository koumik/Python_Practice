# 8) To check whether a number is perfect or not.

n = int(input("Enter any number: "))
s= 0
for i in range(1, n):
    if(n % i == 0):
        s = s + i
if (s == n):
    print("The number is a Perfect number!")
else:
    print("The number is not a Perfect number!")
