# 10) To count the number of lines in a text file


def file_lengthy(numoflines):
        with open(numoflines) as f:
                for i, l in enumerate(f):
                        pass
        return i + 1
print("Number of lines in the file: ",file_lengthy("numoflines.txt"))
