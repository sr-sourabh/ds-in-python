# question 1

def intreverse(n):
	newn = 0
	while(n):
		newn *= 10
		newn += n %10
		n //= 10
	return newn

#question 2

def matched(s):
 c = 0
 for i in s:
  if(i == '('):
   c += 1
  if(i == ')'):
   if(c<1):
    return False
   c -= 1
 if(c == 0 ):
  return True
 else : 
  return False
  
  
#question 3
def sumprimes(l):
  total=0
  for i in l:
    if(isPrime(i)):
      total+=i       
  return(total)
  
def isPrime(n):
  if(n<0):
    return False
  for i in range(2,n):
      if(n%i==0):
        return False
  return True








  
