"""7) To accept a string and
       calculate the number of upper case letters and lower case letters"""


string=raw_input("Enter string:")

x=0
y=0
def check(s):
    global x,y
    for i in string:
        if(i.islower()):
            x=x+1
        print 'Lower Case : ',x
        elif(i.isupper()):
                y=y+1
        print 'Upper Case :', y

check(string)



