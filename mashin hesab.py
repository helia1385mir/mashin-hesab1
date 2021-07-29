
import math
op=input()
if op=='sqrt' or op=='sin' :
    a=float(input())
else:
    a=float(input())
    b=float(input())


if op =='+' :
    result=a+b
elif op=='-':
    result=a-b
elif op=='*' :
    result=a*b
elif op =='/':
    if b==0 :
        result='can not divid by zero'
    else:
        result=a/b
elif op=='^':
    result=a**b
elif op=='sqrt': #radikal
    result=math.sqrt(a)
elif op=='sin':
    result=math.sin(a)
else:
    result='error!operator not found'
print(result)
