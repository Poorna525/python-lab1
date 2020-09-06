#perfect number

#input
n = int(input("enter num: "))
s = 0  
for i in range(1,n-1):
    if n%i==0:
        s += i
if n==s:
    print(n, 'is perfect number')
else:
    print(n, 'is not perfect number')