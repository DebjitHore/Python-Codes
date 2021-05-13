def squares(num):
    return num**2

mynumlist=[1, 2, 3 ,4,5]

newlist=list(map(squares,mynumlist))

print(newlist)

def checkeven(num):
    return num%2==0
newlist2=list(filter(checkeven,mynumlist))
print(newlist2)

newlist3=[]
newlist4=[]
newlist3= list(map(lambda num:num**2,mynumlist))
print(newlist3)
newlist4= list(filter(lambda num:num%2==0,mynumlist))
print(newlist4) 