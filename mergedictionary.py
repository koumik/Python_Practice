# 8) To merge two dictionaries.

x={1:'a',2:'B',3:'k'}
y={1:'abc','K':'Kolkata',5:90}
def merge_dict(x,y):
    c=x.copy()
    c.update(y)
    return c

c=merge_dict(x,y)
print c

