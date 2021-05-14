import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    st=str1.replace(' ','')
    cst=set(st)
    cst2=set(alphabet)
    diff= cst.difference(cst2)
    if diff is None:
      print('The string is pangram')



ispangram("The quick brown fox jumps over the lazy dog")