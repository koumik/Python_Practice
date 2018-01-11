# 2) To determine whether a given year is a leap year.

def leap_year(y):
    if y % 400 == 0:
        print "Leap Year"
        #return True
    if y % 100 == 0:
        print "Not Leap Year"
        #return False
    if y % 4 == 0:
        print "Leap Year"
        #return True
    else:
        print  "Not Leap Year"
        #return False


lp=input("Enter year : ")
print leap_year(lp)

