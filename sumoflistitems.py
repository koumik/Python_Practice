# 1)To find sum of all the items in a list.

sum_list=[]
num=int(input("Total Index Numbers : "))

for n in range(num):
    numbers=int(input("Enter elements of the list : "))
    sum_list.append(numbers)

print "Sum of elements in given list ", sum_list, "is :",sum(sum_list)


