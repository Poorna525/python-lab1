#Concatenate two arrays

#array1
n1 = int(input("Enter length of an array: "))
a1=[]
print("Enter elements: ")
for i in range(0,n1):
	k = int(input())
	a1.append(k) 	
print("Array1 is: ",a1) 

#array2
n2 = int(input("Enter length of an array: "))
a2=[]
print("Enter elements: ")
for i in range(0,n2):
	k = int(input())
	a2.append(k)	
print("Array2 is: ", a2) 

#copying elements 
a3 = a1+a2

print("New Array is: ",a3)