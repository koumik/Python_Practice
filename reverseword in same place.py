#Reverse Words in String in its own place.



s=raw_input("Enter a String: ")
def reverse_words(s):
    reverseWord = " "
    list = s.split()
    for word in list:
        word= word[::-1]
        reverseWord = reverseWord + word + " "
    print reverseWord.strip()

reverse_words(s)
