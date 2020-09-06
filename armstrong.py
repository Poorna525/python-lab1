#armstrong number

#input
n=int(input("enter number: "))
a=n
d=0
s=0
while a!=0:
    s=s+a%10
    d=d+1
    a=a//10
print(s)
a=n
s=0
while a!=0:
    s=s+(a%10)**digits
    a=a//10
if n==s:
    print(n,"is an armstrong number")
else:
    print(n,"is not an armstrong number")