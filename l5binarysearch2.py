#Shifa Mehreen
#121910313005

#Binary search with user defined function and dynamic inputs

#dynamic inputs
def array_input():
	n = int(input("Enter no'of elements: "))
	print("Enter elements: ")
	a = []
	for i in  range(0,n):
		k = int(input())
		a.append(k)
	return a

#function
def binarysearch_array(a):
	a.sort()
	print("Sorted array is: ",a)

#search element
	x = int(input("Enter search element: "))

	loc =0
	low = 0
	high = len(a) - 1
	mid = (low+high)//2

#checking
	if a[mid] == x:
		loc = mid
		f = 1

	elif x < a[mid]:
		for i in range(low,mid):
			if a[i] == x:
				loc = i
				f = 1
				break

	elif x > a[mid]:
		for i in range(mid,high+1):
			if a[i] == x:
				loc = i
				f = 1
				break

    #output
    #if found
    if f == 1:
        print("Element",x,"is found at index",loc)
    #if not found
    else:
        print("Element not found!!")



#function calling 
arr = array_input()
print("Array is: ", arr)
binarysearch_array(arr)