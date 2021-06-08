a=[1,2,'hello',(3,4),{'key':'value'}]

print(a[0])

#output--1

print(a[0],a[3])
#output--1 (3, 4)

print(a[0:5])
#output--[1, 2, 'hello', (3, 4), {'key': 'value'}]
print(a[0:])

#output--[1, 2, 'hello', (3, 4), {'key': 'value'}]
print(a[:-1])

#output--[1, 2, 'hello', (3, 4)]

print(a[0:5:2])
#output--[1, 'hello', {'key': 'value'}]

