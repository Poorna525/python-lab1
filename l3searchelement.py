#Searching an element

n = int(input("Enter length: "))
print("Enter elements: ")
a = []
for i in range(0,n):
	k = int(input())
	a.append(k)
print(a)

#search function
def search(x):
	for i in range(0,n):
		if a[i] == x:
			loc = i 
			print("Found the search element:",x, "at the location:",i)
			break
	else:
		print("Search element:",x,"not found!")
		
l = int(input("Enter the search element: "))

search(l) #calling the "search" function