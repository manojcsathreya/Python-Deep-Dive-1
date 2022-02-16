'''
Functional Equivalents to Operators

In the last lecture we wrote code such as:

l = [2, 3, 4]
reduce(lambda a, b: a * b, l)

We used a lambda expression to create a functional version of the *operator

This is something that happens quite often, so the operator module was created

This module is a convenience module.

You can always use your own functions and lambda expressions instead.


The operator module
Arithmetic Functions

add(a, b)

mul(a, b)

pow(a, b)

mod(a, b)

floordiv(a, b)

neg(a)


and many more…



Comparison and Boolean Operators

lt(a, b)       gt(a, b)
                
le(a, b)       ge(a, b)

and_(a, b)
or_(a,b)

eq(a, b)
ne(a, b)

is_(a,b) is_not(a,b)

not_(a,b)


Sequence/Mapping Operators

concat(s1, s2)

contains(s, val)

countOf(s, val)

getitem(s, i)

setitem(s, i, val)
                    -------------- mutable objects
delitem(s, i)

Item Getters

The itemgetter function returns a callable

getitem(s, i) takes two parameters, and returns a value: s[i]

s = [1, 2, 3]

getitem(s, 1) → 2

itemgetter(i)  returns a callable which takes one parameter: a sequence object

s = [1, 2, 3]

f = itemgetter(1)

f(s) → 2

s = 'python'

f(s) → 'y'

Item Getters

We can pass more than one index to itemgetter:

l = [1, 2, 3, 4, 5, 6]
s = 'python'

f = itemgetter(1, 3, 4)

f(l)  → (2, 4, 5)

f(s) → ('y', 'h', 'o')

Attribute Getters

The attrgetter function is similar to itemgetter, but is used to retrieve object attributes
It also returns a callable, that takes the object as an argument

Suppose my_objis an object with three properties:
my_obj.a → 10
my_obj.b → 20
my_obj.c → 30

f = attrgetter('a') f(my_obj) → 10

f = attrgetter('a', 'c') f(my_obj) → (10, 30)

Can also call directly:
attrgetter('a', 'b', 'c')(my_obj) → (10, 20, 30)
------------------------------------------------------------------------
Calling another Callable
Consider the strclass that provides the upper() method:
s = 'python' s.upper() → PYTHON

f = attrgetter('upper')
f(s) →returns the uppermethod of s
it is a callable, and can be called using ()
f(s)() → PYTHON
attrgetter('upper')(s)() → PYTHON
Or, we can use the slightly simpler methodcaller function
methodcaller('upper')('python') → PYTHON
Basically, methodcaller retrieves the named attribute and calls it as well
It can also handle more arguments, as we'll in the code
'''

import operator
operator.add(2,3)#5
operator.mul(2,3)#6
operator.truediv(3, 2)#1.5
operator.floordiv(13, 2)#6

from functools import reduce
reduce(lambda a,b:a*b,[1,2,3,4]) #24

reduce(operator.mul,[1,2,3,4]) #24

operator.lt(10,3)#Flase

from operator import is_
is_('abc','def') #Flase

is_('abc','abc')# True

my_list = [1,2,3,4]

operator.getitem(my_list, 2) #3

my_list[1]=100
my_list #[1, 100, 3, 4]

del my_list[3]
my_list #[1, 100, 3]

mylist = [1,2,3,4]
operator.setitem(mylist, 1, 100)
mylist #[1,100,3,4]

operator.delitem(mylist, 3)
mylist #[1, 100, 3]

f = operator.itemgetter(2)
type(f) #operator.itemgetter

mylist = [1,2,3,4]
s = 'python'
f(mylist) #3
f(s)#'t'

f = operator.itemgetter(2,3)
f([1,2,3,4]) # (3,4)
f('Python') #('t','h')


class myclass:
    
    def __init__(self):
        self.a = 10
        self.b=20
        self.c = 30
        
    def test(self):
        print('test method running.....')
        
obj = myclass()
obj #<__main__.myclass at 0x28704a490a0>

obj.a#10
obj.test #<bound method myclass.test of <__main__.myclass object at 0x0000028704A490A0>>
obj.test() #test method running.....

f = operator.attrgetter('a')
f(obj) #10

myvar = 'b'
f = operator.attrgetter(myvar)
f(obj) #20
myvar = 'c'
f(obj) #20 and you know why

a,b,test = operator.attrgetter('a','b','test')(obj)
print(a) #10
print(b) #20
print(test()) #test method running.....

f = lambda x:x.a
f(obj) #10

#Use Case Example: Sorting
#Suppose we want to sort a list of complex numbers based on the real part of the numbers:
a = 2 + 5j
a.real #2.0

l = [10+1j, 8+2j, 5+3j]

sorted(l,key=lambda x: x.real) #[(5+3j), (8+2j), (10+1j)]
sorted(l, key=operator.attrgetter('real')) #[(5+3j), (8+2j), (10+1j)]

#Or if we want to sort a list of string based on the last character of the strings:
l = ['aaz', 'aad', 'aaa', 'aac']
sorted(l, key = operator.itemgetter(-1)) #['aaa', 'aac', 'aad', 'aaz']

l = [(2, 3, 4), (1, 2, 3), (4, ), (3, 4)]
sorted(l, key=operator.itemgetter(0))
#[(1, 2, 3), (2, 3, 4), (3, 4), (4,)]

class myclass:
    
    def __init__(self):
        self.a = 10
        self.b=20
        self.c = 30
        
    def test(self):
        print('test method running.....')
        
        
f = operator.methodcaller('test')
f(obj) #test method running.....


class myclass:
    
    def __init__(self):
        self.a = 10
        self.b=20
        self.c = 30
        
    def test(self,c):
        print(self.a,self.b,c)

obj = myclass()
f= operator.methodcaller('test')        
f(obj) #TypeError: test() missing 1 required positional argument: 'c'
operator.methodcaller('test',100)(obj) #10 20 100

class myclass:
    
    def __init__(self):
        self.a = 10
        self.b=20
        self.c = 30
        
    def test(self,c,d,*,e):
        print(self.a,self.b,c,d,e)

obj = myclass()

operator.methodcaller('test',100,200,e = 300)(obj) #10 20 100 200 300

f = operator.attrgetter('test')
f(obj)(100,200,e=300) #10 20 100 200 300
