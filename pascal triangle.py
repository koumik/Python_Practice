# 9) To print out the first n rows of Pascal's triangle

rows=input("Enter Rows of pascal triangle : ")


def pascal_triangle(n):
   f = [1]
   y = [0]
   for x in range(max(n,0)):
      print(f)
      f=[l+r for l,r in zip(f+y, y+f)]
   return n>=1

pascal_triangle(rows) 
