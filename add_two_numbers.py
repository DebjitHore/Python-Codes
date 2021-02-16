import random
a= input("Enter a no of your choice")
b= input("Enter a second no of your choice")
sum = a+b
print('The sum of two numbers is {}'.format(sum) )


#square root of user input number.
square_root= a**0.5
print('The square root of {}  is {}'.format(a, square_root) )

#generate random number
c= random.randint(1, 100)
print('A random number in range of 1 to 100 is {}'.format(c)) 

#check prime number or not, we're checking b here.
for i in range (2,b-1,1):
    if ( b%i==0):
        print('The number {} is not prime'.format(b))
        break
    else:
        print('Prime Number')
        break

#


