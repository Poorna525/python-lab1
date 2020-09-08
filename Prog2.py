#121910313062
#POORNA CHANDRA

#removing duplicates

#removing duplicates

#array1
a1 = [1,2,3,4,4,5,5,8,9,8,8,10]
print("Array1 is: ",a1) 

#function
def remove(a1):
	a2=[]
	for num in a1:
		if num not in a2:
			a2.append(num)
	return a2

print("New Array is: ",remove(a1))