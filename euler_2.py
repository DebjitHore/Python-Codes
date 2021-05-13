a=1
b=2
term = 0
sum=2

while (term<4000000):
    term=a+b
    a=b
    b=term
    if(term%2==0):
        sum=sum+term
print(sum)
