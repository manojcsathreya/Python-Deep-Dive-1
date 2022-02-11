'''
Reducing Functions in Python
These are functions that recombine an iterable recursively, ending up with a single return value
Also called accumulators, aggregators, or folding functions.

Example: Finding the maximum value in an iterable
a0, a1, a2, …, an-1



max(a, b) →maximum of aand b
result = a0
result = max(result, a1)
result = max(result, a2)
…
result = max(result, an-1)    →max value in a0, a1, a2, …, an-1

Because we have not studied iterables in general, we will stay with the special case of sequences. 
(i.e. we can use indexes to access elements in the sequence)

Using a loop
l = [5, 8, 6, 10, 9]
max_value = lambda a, b: a if a > b else b

def max_sequence(sequence):
    result = sequence[0]
    for e in sequence[1:]:
        result = max_value(result, e)
    return result

result = 5
result = max(5, 8) = 8
result = max(8, 6) = 8
result = max(8, 10) = 10
result = max(10, 9) = 10
result → 10

To calculate the min:
l = [5, 8, 6, 10, 9]

min_value = lambda a, b: a if a < b else b

def min_sequence(sequence):
    result = sequence[0]
    for e in sequence[1:]:
        result = min_value(result, e)
    return result

In fact we could write:
def _reduce(fn, sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = fn(result, x)
    return result

All we really needed to do was to change 
the function that is repeatedly applied.

_reduce(lambda a, b: a if a > b else b, l) → maximum
_reduce(lambda a, b: a if a < b else b, l) → minimum

Adding all the elements in a list

add = lambda a, b: a+b

l = [5, 8, 6, 10, 9]

def _reduce(fn, sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = fn(result, x)
    return result


_reduce(add, l)

result = 5
result = add(5, 8) = 13
result = add(13, 6) = 19
result = add(19, 10) = 29
result = add(29, 9) = 38
result → 38

The functools module

Python implements a reducefunction that will handle any iterable, but works similarly to what 
we just saw

from functools import reduce

l = [5, 8, 6, 10, 9]

reduce(lambda a, b: a if a > b else b, l) → max → 10
reduce(lambda a, b: a if a < b else b, l) → min → 5
reduce(lambda a, b: a + b, l) → sum → 38


reduceworks on any iterable

reduce(lambda a, b: a if a < b else b, {10, 5, 2, 4}) → 2

reduce(lambda a, b: a if a < b else b, 'python') → h

reduce(lambda a, b: a + ' ' + b, ('python', 'is', 'awesome!'))
→ 'python is awesome'


Built-in Reducing Functions

Python provides several common reducing functions:

min min([5, 8, 6, 10, 9]) →5
max max([5, 8, 6, 10, 9]) →10
sum sum([5, 8, 6, 10, 9]) →38

any any(l) → Trueif any element in lis truthy
Falseotherwise

all all(l) → Trueif every element in lis truthy
Falseotherwise


Using reduceto reproduce any

l = [0, '', None, 100]

result = bool(0) or bool('') or bool(None) or bool(100)

Here we just need to repeatedly apply the oroperator to the truth values of each element
result = bool(0) → False
result = result or bool('') → False
result = result or bool(None) → False
result = result or bool(100) → True

reduce(lambda a, b: bool(a) or bool(b), l)  → True

Note: 0 or '' or None or 100 → 100 but we want our result to be True/False
so we use bool()


Calculating the product of all elements in an iterable

No built-in method to do this

But very similar to how we added all the elements in an iterable or sequence:

[1, 3, 5, 6] → 1 * 3 * 5 * 6

reduce(lambda a, b: a * b, l)



res = 1
res = res * 3 = 3
res = res * 5 = 3 * 5 = 15
res = res * 6 = 15 * 6 = 90
= 1 * 3 * 5 * 6

Special case: Calculating n!

n! = 1 * 2 * 3 * … * n 

5! = 1 * 2 * 3 * 4 * 5

range(1, 6) → 1, 2, 3, 4, 5

range(1, n+1) → 1, 2, 3, …, n

To calculate n!we need to find the product of all the elements in range(1, n+1)

reduce(lambda a, b: a * b, range(1, 5+1)) →5!


The reduceinitializer

The reducefunction has a third (optional) parameter: initializer (defaults to None)
If it is specified, it is essentially like adding it to the front of the iterable.
It is often used to provide some kind of default in case the iterable is empty.
l = []
reduce(lambda x, y: x+y, l) →exception
l = []
reduce(lambda x, y: x+y, l, 1) →1

l = [1, 2, 3]
reduce(lambda x, y: x+y, l, 1) →7
l = [1, 2, 3]
reduce(lambda x, y: x+y, l, 100) →106

'''
l = [5,6,10,8,7]

_max = lambda x,y: x if x>y else y

def _maxsequence(l):
    result = l[0]
    for x in l[1:]:
        result = _max(result,x)
    return result

_maxsequence(l) #10

_min = lambda x,y: x if x<y else y

def _minsequence(l):
    result = l[0]
    for x in l[1:]:
        result = _min(result,x)
    return result

_minsequence(l) #5

_add = lambda x,y:x+y

def _addsequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _add(result,x)
    return result

_addsequence(l)#36

def _reduce(fn,sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = fn(result,x)
    return result

_reduce(lambda x,y: x if x>y else y, l)#10     
_reduce(lambda x,y: x if x<y else y, l)#5
_reduce(lambda x,y:x+y,l)#36

#note this cannot be used for sets coz they are not indexible

_reduce(lambda x,y:x+y,{1,2,3,4,5}) #TypeError: 'set' object is not subscriptable
#but this does not happen in reduce in-built function

from functools import reduce
reduce(lambda x,y: x if x>y else y, l)#10     
reduce(lambda x,y: x if x<y else y, l)#5
reduce(lambda x,y:x+y,l)#36
reduce(lambda x,y:x+y,{1,2,3,4,5}) #15
#FACT: Reduce function does not use indexing for reduce functions

s = {True, None, 0, 1}
all(s) #False
any(s) #True
#all is equivalent to 
bool(s[1]) or bool(s[2]) or bool(s[3]) or bool(s[4]) 
bool(s[1]) and bool(s[2]) and bool(s[3]) and bool(s[4]) 


reduce(lambda x,y:bool(x) and bool(y),s) #False --- ALL FUNCTION IMPLEMENTATION
reduce(lambda x,y:bool(x) or bool(y),s) #True  ---- ANY FUNCTION IMPLEMENTATION


#FActorial Function
reduce(lambda x,y:x*y,range(1,5+1)) #120

#Generic
def fact(n):
    return reduce(lambda x,y:x*y,range(1,n+1))
    
fact(10) #3628800

#initalizers
#say we pass an empty sequence what happens?
reduce(lambda x,y:x+y,[]) #TypeError: reduce() of empty sequence with no initial value

reduce(lambda x,y:x+y,[],0) #0
