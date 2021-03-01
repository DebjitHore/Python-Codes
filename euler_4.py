import math
n2=0
num_list=[]
for j in range(100, 999):
    for k in range(100,999):
        num=j*k
        n= j*k
        i= int(math.log10(num))  #gives no of digits in current num
        while (num>0):
            t= num%10
            n2=n2+t*(10**i)
            i-=1
            num= num/10
        if(n2==n):
            num_list.append(n2)
        n2=0
answer= max(num_list)
print(answer)


 
