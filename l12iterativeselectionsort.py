#Selection Sort (iterative)

a = list(map(int,input().split()))
  
for i in range(len(a)): 
    min_num = i 

    for j in range(i+1, len(a)):
        if a[min_num] > a[j]: 
            min_num = j 

    a[i], a[min_num] = a[min_num], a[i] 

print ("Sorted array: ", a)  