""" 3) To count the number of strings where the string length is 2 or more and
                     the first and last character are same from a given list of strings. """

#str_list=['ab','abc','xyz',213,9000,'ui','aab','acb']




def com(word):
  x = 0

  for i in word:
    if len(i) > 1 and i[0] == i[-1]:
      x+= 1
  return x

print(com(['abc', 'xyz', 'aba', '1221','aba','543212345']))
