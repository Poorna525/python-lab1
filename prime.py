#prime number

#input
n=int(input("enter num: "))
for i in range(2,n+1):
    p=0
    for j in range(2,i-1):
        if i%j==0:
            p=1
            break
    if p==1:
        print(i)