re=[i for i in range(0,10)]
print(re)
a=[1,2,3,4,5]
wee=[i for i in a if i<4 ]
print(wee)
b=[50,45,30,60,80]
well=[i for i in b if i%2==0]
print(well)
c=["hello","world","python"]
rezz=[i.upper() for i in c]
print(rezz)

keys=["name",'age','city']
values=["alice",25,"hyderabad"]
dic5={k:v for k,v in zip(keys,values)}
print(dic5)  #output: {'name': 'bangalore', 'age': 25