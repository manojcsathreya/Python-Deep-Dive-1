'''
To compare objects (WRT address) : We use identity operator
ex : var1 is var2
negation: var1 is not var2
            not (var1 is var2)

To compare internal data of object we use euality operator
ex var1== var2 var1!=var2
'''

a =10
b=10
print(id(a)) #140730006972496
print(id(b)) #140730006972496
print('a is b ', a is b) # a is b  True
print('a == b', a==b) # a == b True


a =500
b=500
print(id(a)) #2157326350640
print(id(b)) #2157326349104
print('a is b ', a is b) # a is b  False
print('a == b', a==b) # a == b True


a = [1,2,3]
b =[1,2,3]
print(id(a)) #2157312597376
print(id(b)) #2157312596032
print('a is b ', a is b) # a is b  False
print('a == b', a==b) # a == b True


a =10.0
b =10
print(id(a)) #2157326348496
print(id(b)) #140730006972496
print('a is b ', a is b) # a is b  False
print('a == b', a==b) # a == b True

