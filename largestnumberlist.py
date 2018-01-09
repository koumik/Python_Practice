# 2)To get the largest number from a list.

alist=[]
index=input("Total Index Numbers : ")

for i in range(index):
    num=input("Enter Elements of the List : ")
    alist.append(num)

print "The List is : ", alist

sort_list=sorted(alist)
print "Sorted List is : ", sort_list

large_number=max(sort_list)
print "Largest Number is the List is : ", large_number

