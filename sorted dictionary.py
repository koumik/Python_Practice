# Sorted Dictionary in ascending and descending order.

import operator

d= {1:2,3:4,4:2,2:1,0:0}

print ('Original Dictionary: ',d)
sorted_d=sorted(d.items())
print 'In ascending order : ' ,sorted_d
sorted_d=sorted(d.items(), reverse=True)
print 'In descending order :', sorted_d
