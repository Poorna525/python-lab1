#POORNA CHANDRA
#121910313062

#represent a sparse matrix

#matrix initialization
matrix = ([0,0,0,2],
	      [8,0,0,4],
	      [2,0,4,0],
	      [0,0,0,2])
#printing initialized matrix
print("Given Matrix: ")
for i in matrix:
	for j in i:
		print(j, end=" ")
	print()

#SparseMatrix

sparsematrix = [] 

for i in range(len(matrix)):
	for j in range(len(matrix[0])):
		if matrix[i][j] != 0:

			temp=[]

			temp.append(i) #row index
			temp.append(j) #column index
			temp.append(matrix[i][j]) 

			sparsematrix.append(temp)

#printing SparseMatrix
print("\nSparseMatrix: ")
for i in sparsematrix:
	for j in i:
		print(j, end =" ")
	print()