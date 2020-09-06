#printing primes

#input
k = int(input("Enter a limit: "))

#logic

#function
def prime(n): 
	count = 0
	for i in range(1,n+1): 
		if n%i == 0:
			count = count + 1
	if count == 2: 
		return True
	else: 
		return False 

#printing 
for n in range(1,k+1):
	if prime(n) is True:
		print(n)

