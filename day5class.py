"""result = lambda x,y:x+y
result1 = lambda x,y:x-y
result2 = lambda x,y:x*y
x=int(input("Enter x: "))
y=int(input("Enter y: "))
print(result(x,y))
print(result1(x,y))
print(result2(x,y))"""

#without generator
l=[1,2,3,4]
for i in l:
    print(i)
iterable=iter(l)
print(iterable)