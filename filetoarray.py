# 9) To read a file line by line store it into an array



def file_read(fname):
        content_array = []
        with open(fname) as f:
                   
                for line in f:
                        content_array.append(line)
                print(content_array)

file_read('filetoarray.txt')
