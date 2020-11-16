#Implement the parenthesis matching algorithm using stack

def Parenthesischecker(s):
  stack=[]
  o="{[("
  c="}])"
  for i in s:
    if i in o:
      stack.append(i)
    else:
      if len(stack)==0:
        return False
      else:
        if c.index(i)==o.index(stack[-1]):
          stack.pop()
    print(*stack)
  if len(stack)==0:
    return True
  return False
  
s=input("Enter a string of braces: ")
t=Parenthesischecker(s)
print(t)
		
