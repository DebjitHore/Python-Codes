num= input('Enter the range')
x=0
for i in range(2, num-1):
    if (num%i == 0):
        x=1
        break
        
if (x==0):
    print('Prime')
else: 
    print('Not Prime')