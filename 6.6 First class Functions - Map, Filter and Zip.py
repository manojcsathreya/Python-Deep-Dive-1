'''
Higher order functions

A function that takes a function as a parameter and/or returns a function as its return value

Example: sorted

map
                -- modern alternative →list comprehensions and generator expressions
filter
---------------------------------------------------------------------------
The mapfunction

map(func, *iterables)

func →some function that takes as many arguments as there are iterable
objects passed to iterables

*iterables →a variable number of iterable objects

map(func, *iterables) will then return an iterator that calculates the 
function applied to each element of the iterables

The iterator stops as soon as one of the iterables has been exhausted
so, unequal length iterables can be used

Examples
l = [2, 3, 4]
def sq(x):
return x**2

list(map(sq, l)) → [4, 9, 16]

l1 = [1, 2, 3]
l2 = [10, 20, 30]
def add(x, y):
return x + y
list(map(add, l1, l2)) → [11, 22, 33]

list(map(lambda x, y: x + y, l1, l2)) → [11, 22, 33]
---------------------------------------------------------------------------
The filter function

filter(func, iterable)

func →some function that takes a single argument

iterable →a single iterable

filter(func, iterable) will then return an iterator that contains all the 
elements of the iterable for which the function called on it is Truthy

If the function is None, it simply returns the elements of iterable that are Truthy

Examples

l = [0, 1, 2, 3, 4]

list(filter(None, l)) → [1, 2, 3, 4]

def is_even(n):
    return n % 2 == 0

list(filter(is_even, l)) → [0, 2, 4]

list(filter(lambda n: n % 2 == 0, l)) → [0, 2, 4]
---------------------------------------------------------------------------
The zipfunction

[1, 2, 3, 4]
[10, 20, 30, 40]

zip

(1, 10), (2, 20), (3, 30), (4, 40)

[1, 2, 3]
[10, 20, 30] zip (1, 10, 'a'), (2, 20, 'b'), (3, 30, 'c')
['a', 'b', 'c']

[1, 2, 3, 4, 5]
[10, 20, 30]

zip

(1, 10), (2, 20), (3, 30)

zip(*iterables)
Examples

l1 = [1, 2, 3]
l2 = [10, 20, 30, 40]
l3 = 'python'
list(zip(l1, l2, l3)) → [(1, 10, 'p'), (2, 20, 'y'), (3, 30, 't')]

l1 = range(100)
l2 = 'abcd'
list(zip(l1, l2)) → [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]
---------------------------------------------------------------------------

List Comprehension Alternative to map

l = [2, 3, 4]

def sq(x):
    return x**2
list(map(sq, l)) → [4, 9, 16]

result = []
for x in l:
    result.append(x**2) 
    result                  → [4, 9, 16]

[x**2 for x in l] → [4, 9, 16]

SYNTAX
[<expression> for <varname> in <iterable>]

list(map(lambda x: x**2, l))

---------------------------------------------------------------------------
List Comprehension Alternative to map

l1 = [1, 2, 3]
l2 = [10, 20, 30]

list(map(lambda x, y: x + y, l1, l2)) → [11, 22, 33]

[x + y for x, y in zip(l1, l2)] → [11, 22, 33]

Remember: zip(l1, l2) → [(1, 10), (2, 20), (3, 30)]

List Comprehension Alternative to filter

l = [1, 2, 3, 4]
list(filter(lambda n: n % 2 == 0, l)) → [2, 4]

[x for x in l if x % 2 == 0] → [2, 4]

[<expression1> for <varname> in <iterable> if <expression2>]

-------------------------------------------------------------------------------
Combining mapand filter

l = range(10)
list(filter(lambda y: y < 25, map(lambda x: x**2, l))) → [0, 1, 4, 9, 16]

Using a list comprehension is much clearer:

[x**2 for x in range(10) if x**2 < 25] → [0, 1, 4, 9, 16]



'''

def fact(n):
    return 1 if n<2 else n*fact(n-1)

fact(3) #6
fact(4) #24

result = map(fact,(range(6)))
#here map function returns an generator and we can iterate over that
print(result) #<map object at 0x0000016B48154790>

for x in result:
    print(x)
    
"""
1
1
2
6
24
120
"""
#now if we call the generators for the second time
for x in result:
    print(x) #it prints nothing
    
#but why?
#Python implements lazy evaluation. It does not evaluate until the values are called. And once the values are called, thats it. It is done.
#so better get the elements and make it into a list

def fact(n):
    return 1 if n<2 else n*fact(n-1)

fact(3) #6
fact(4) #24

result = list(map(fact,(range(6))))
print(result) #[1, 1, 2, 6, 24, 120]

l1=[1,2,3]
l2 = [10,20,30,40,50]
l3 = 100,200,300,400
#
result = list(map(lambda x,y,z:x+y+z, l1,l2,l3))
print(result)#[111, 222, 333]
#Execution stops as soon as the shortest gets over
#proff that map function returns a generator

result = map(lambda x,y,z:x+y+z,l1)
print(result)#<map object at 0x0000016B481090A0>
#Runs without any error
for x in result:
    print(x) #TypeError: <lambda>() missing 2 required positional arguments: 'y' and 'z'
    
x = range(0,25)
print(x) #range(0, 25) - Same - it does not get evaluated until it is called

for i in x:
    print(i)
    
    # no matter how many times we call this , this always return value unlike generators

#Zip

l1 = [1,2,3,4]
l2 = 100,200,300
l3 = 'python'

#Zip also return generators. So we make it a list

list(zip(l1,l2,l3)) #[(1, 100, 'p'), (2, 200, 'y'), (3, 300, 't')]
list(zip(range(10000),'python')) #[(0, 'p'), (1, 'y'), (2, 't'), (3, 'h'), (4, 'o'), (5, 'n')]

results = (fact(n) for n in range(10))
print(results)#<generator object <genexpr> at 0x0000016B481906D0>
#list comprehensions are making the list of items returned from generators
#instead of list(genrator), we use [generator] both are same

results = [fact(n) for n in range(10)]
results #[1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]


l1 = 1,2,3,4,5,6
l2 = 10,20,30,40

list(map(lambda x,y:x+y,l1,l2)) #[11, 22, 33, 44]
#how to in list comprehension

res = [x+y for x,y in zip(l1,l2)]
res #[11, 22, 33, 44]

res = list(filter(lambda x: x%2==0, map(lambda x,y:x+y,l1,l2)))
print(res) #[22, 44]

res1 = [x+y for x,y in zip(l1,l2) if (x+y)%2==0]
res1 # [22, 44]


