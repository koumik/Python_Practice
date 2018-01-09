# To read an entire text file

"""fileobj=open("assignment.txt",'w+')
#l=len(fileobj)
????????Didnt worked out????

print "Information in the File : \n", fileobj.read()

fileobj.close()"""


def file_read(fname):
    txt=open(fname)
    print (txt.read())

file_read('assignment.txt')
