num= 60085147514

term=0
counter=0
counter2=0
for i in range (2, num):
    if (num% i == 0):
        counter2=1
        for j in range(2, i):
            if(i%j == 0 ):
                counter=1
        if (counter == 0):
            term= i
        else: 
            continue
    if (counter2==0):
        term= num
print(term)
         
  