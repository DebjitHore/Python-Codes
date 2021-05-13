def count_primes(num):
  count=1 
  for i in range (3,num):
    for j in range (2, i):
      
      if i%j==0:
        break
    else:
      count+=1
  print('The total number of primes in range {} is {}'.format(num, count))
  
  
  
  
count_primes(100)