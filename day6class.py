"""result = lambda x,y:x+y
result1 = lambda x,y:x-y
result2 = lambda x,y:x*y
x=int(input("Enter x: "))
y=int(input("Enter y: "))
print(result(x,y))
print(result1(x,y))
print(result2(x,y))"""

#without generator
"""l=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for i in l:
    if i%2==0:
        print(i)
iterable=iter(l)
print(iterable)
for i in iterable:
    print(i)"""

#check the below code list and display the string were the string letter is start with 'a' letter or contain 'a' letter with iterter
"""m=["apple","banana","cherry","date","elderberry","fig","grape"]
for i in m:
    if i[0]=="a":
        print(i)
iterable=iter(m)
print(iterable)
for i in iterable:
    if "a" in i:
        print(i)"""



