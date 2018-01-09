# 6) To check whether a number is in a given range


def test_range(n):
    if n in range(1,11):
        print( " %s is in the range"%str(n))
    else :
        print("The number is outside the given range")

num=input("Enter Range :")
test_range(num)
