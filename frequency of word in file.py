#11) To count the frequency of words in a file

from collections import Counter

def word_count(filename):
        with open(filename) as f:
                return Counter(f.read().split())

print("Number of words in the file :",word_count("frequency.txt"))
