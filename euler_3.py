num= 50
term=0
i=2
j=2
for i in range (2, num):
    if(num%i==0):
        for j in range (2, i):
            if(i%j != 0):
                term=i
        
print(term)