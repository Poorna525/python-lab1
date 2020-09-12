
#operations on array

#input of array
print("Enter length: ")
n = int(input())
print("Enter elements: ")
a = []
for i in range(0,n):
	k = int(input())
	a.append(k)

#display
def display_element():
	print("Array is: ",a)

#copy
def copy_element():
	a1 = a
	print("Copied array: ",a1)

#delete
def delete_element():
	print("Enter the index: ")
	y = int(input())
	del a[y]
	print("New Array: ",a)

#search
def search_element():
	print("Enter the search element: ")
	l = int(input())
	for i in range(0,n):
		if a[i] == l:
			loc = i
			print("Element: ",l,"is found at index: ",loc)
			break
	else:
		print("Element not found!!")

#removing
def remove_duplicate_element():
	a1=[]
	for i in a:
		if i not in a1:
			a1.append(i)
	print("New Array is: ",a1)

#choices
print("Choose: \n 1:to display \n 2:to copy \n 3:to remove duplicates \n 4:to delete \n 5:to search")

print("Enter choice: ")
q = int(input())

#selection
if (q == 1):
	display_element()
elif (q == 2):
	copy_element()
elif (q == 3):
	remove_duplicate_element()
elif (q == 4):
	delete_element()
elif (q == 5):
	search_element()
else:
	print("Enter a right number from 1 to 5!")