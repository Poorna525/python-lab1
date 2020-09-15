#POORNA CHANDRA
#121910313062

#Matrix to SparseMatrix using functions
#and taking input from user

#input 
def input_matrix():
    r= int(input("Enter the number of rows: ")) 
    c = int(input("Enter the number of columns: ")) 
      
    matrix = []

    print("Enter elements: ") 
     
    for i in range(r):          
        a =[] 
        for j in range(c):
            k = int(input())
            a.append(k)
        matrix.append(a)
    return matrix

def display_matrix(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()

def sparseMatrix(matrix):
    

    l = int(input("Enter threshold value: "))

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] <l+1:
                matrix[i][j] = 0

    sparsematrix = [] 

    #looping
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:

                temp=[] 

                temp.append(i) 
                temp.append(j) 
                temp.append(matrix[i][j])

                sparsematrix.append(temp)

    print("\nSparseMatrix:")
    display_matrix(sparsematrix)



#input matrix
x= input_matrix()
print("Given Matrix: ")
display_matrix(x)

#conversion
sparseMatrix(x)