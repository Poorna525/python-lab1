#linear search without functions

a = [5, 34, 22, 90, 12]

print("Array is: ",a)

x = int(input("Enter search element: "))

loc = 0
for i in range(0,len(a)):
	if a[i] == x:
		loc = i
		print("Element",x,"is found at index",loc)
		break
else:
	print("Element not found!!")