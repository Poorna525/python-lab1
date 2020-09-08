#121910313062
#POORNA CHANDRA

#copying and array into another empty array

#array1
a1 = [1,2,3,4,5]
print("Array1 is: ",a1) 

#array2

a2 = [None]*len(a1) #declaring another array2 
                    #with same length as array1

for i in range(0,len(a1)):
	a2[i] = a1[i] #copying

print("Array2 is: ",a2)