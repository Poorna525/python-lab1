#Binary search

a = [62, 55, 64, 32, 9, 54, 45]
a.sort()
print("Array is: ",a)

x = int(input("Enter search element: "))

loc =0
low = 0
high = len(a) - 1
mid = (low+high)//2

if a[mid] == x:
	loc = mid
	print("Element",x,"is found at index",loc)

elif x < a[mid]:
	for i in range(low,mid):
		if a[i] == x:
			loc = i
			print("Element",x,"is found at index",loc)
			break
	else:
		print("Element not found!!")

elif x > a[mid]:
	for i in range(mid,high+1):
		if a[i] == x:
			loc = i
			print("Element",x,"is found at index",loc)
			break
	else:
		print("Element not found!!")

else:
	print("Element not found!!")