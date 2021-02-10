st = 'Print only the words that start with s in this sentence'
str= ' '
for n in st.split():
    if n[0]=='s':
        str= str+n+' '
print(str)
