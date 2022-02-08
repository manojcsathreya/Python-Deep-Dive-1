'''
Callables

What are callables?
any object that can be called using the ()operator

like functions and methods but it goes beyond just those two…

many other objects in Python are also callable

To see if an object is callable, we can use the built-in function: callable
callable(print) → True
callable('abc'.upper) → True

callable(str.upper) → True

callable(callable) → True

callables always return a value

callable(10) → False

Different Types of Callables

built-in                     --   print len callable
built-in methods             --   a_str.upper a_list.append
user-defined functions       --   created using defor lambdaexpressions
methods                      --   functions bound to an object
classes                      --   MyClass(x, y, z)
                                  → __new__(x, y, z) →creates the new object
                                  → __init__(self, x, y, z)
                                  →returns the object (reference)

class instances              --   if the class implements __call__ method
generators, coroutines, asynchronous generators 
'''

"""
A callable is an object that can be called (using the () operator), and always returns a value.

We can check if an object is callable by using the built-in function callable
"""

callable(print) #True
callable(len) #True
l = [1,2,3,4]
callable(l.append)#True
s = 'abc'
callable(s.upper())#False. We are calling the function here, so it returns a string and strings are not callable
callable(s.upper)#True


#Callables always returns a value
result = print('hello') #hello
print(result) #None

l = [1,2,3,4]
result = l.append(5)
print(result) #None
print(l) #[1, 2, 3, 4, 5]

s = 'abc'
result = s.upper()
print(result) #ABC

#Classes are callables
from decimal import Decimal
callable(Decimal)#true
a = Decimal('10.5')
print(callable(a))#False

#class instances maybe callable

class MyClass:
    def __init__(self,x = 0):
        print('initializing...')
        self.counter = x
        
callable(MyClass) #True

a = MyClass(100)
callable(a) #False

#tomake an instance callable we have a special method, __call__

class MyClass:
    def __init__(self,x = 0):
        print('initializing...')
        self.counter = x
    
    def __call__(self,x = 1):
        print('Updating counter') 
        self.counter+=1
        
b = MyClass(100)
MyClass.__call__(b,10) #Updating counter
b.counter #101
callable(b) #true
b(1000) #Updating counter
b.counter #102
