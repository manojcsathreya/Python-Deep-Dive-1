# Decorator Application
#Memoization- Allows us to build cache 
#Let's go back to our Fibonacci example:
def fib(n):
    print ('Calculating fib({0})'.format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)

fib(6)
'''
Calculating fib(6)
Calculating fib(5)
Calculating fib(4)
Calculating fib(3)
Calculating fib(2)
Calculating fib(1)
Calculating fib(2)
Calculating fib(3)
Calculating fib(2)
Calculating fib(1)
Calculating fib(4)
Calculating fib(3)
Calculating fib(2)
Calculating fib(1)
Calculating fib(2)
Out[68]: 8

It would be better if we could somehow "store" these results, so if we have calculated fib(4) and fib(3) before, we could simply recall the these values when calculating fib(5) = fib(4) + fib(3) instead of recalculating them.

This concept of improving the efficiency of our code by caching pre-calculated values so they do not need to be re-calcualted every time, is called "memoization"

We can approach this using a simple class and a dictionary that stores any Fibonacci number that's already been calculated:

'''
class Fib:
    def __init__(self):
        self.cache = {1:1,2:1}
        
    def fib(self,n):
        if n not in self.cache:
            print('Calculating fib {0}'.format(n))
            self.cache[n] = self.fib(n-1)+self.fib(n-2)
        return self.cache[n]
    

f = Fib()

f.fib(6)
'''
Calculating fib 6
Calculating fib 5
Calculating fib 4
Calculating fib 3
Out[70]: 8
'''
f.fib(7)
'''
Calculating fib 7
Out[71]: 13
'''

#Let's see how we could rewrite this using a closure:
    
def fib():
    cache = {1:1,2:1}
    
    def calc_fib(n):
        if n not in cache:
            print('Calculating fib({0})'.format(n))
            cache[n] = calc_fib(n-1) + calc_fib(n-2)
        return cache[n]
    return calc_fib 

f = fib()
f(10)
'''
Calculating fib(10)
Calculating fib(9)
Calculating fib(8)
Calculating fib(7)
Calculating fib(6)
Calculating fib(5)
Calculating fib(4)
Calculating fib(3)
Out[73]: 55
'''

f(11)
'''
Calculating fib(11)
Out[74]: 89
'''

#Let us implement the same using Decorators

def memoization_fib(fn):
    cache = {1:1,2:1}
    
    def inner(n):
        if n not in cache:
            cache[n] = fn(n)
        return cache[n]
    
    return inner 

@memoization_fib 
def fib(n):
    print('calculating fib {0}'.format(n))
    return 1 if n<=2 else fib(n-1)+fib(n-2)

fib(5)
'''
calculating fib 5
calculating fib 4
calculating fib 3
Out[77]: 5
'''
fib(7)
'''
calculating fib 7
calculating fib 6
Out[78]: 13
'''

#same we can do for fact function or Generalized way

def memoization(fn):
    cache = dict()
    
    def inner(n):
        if n not in cache:
            cache[n] = fn(n)
        return cache[n]
    
    return inner 

@memoization 
def fact(n):
    print('Calculating {0}!'.format(n))
    return 1 if n==1 else n*fact(n-1) 
       
fact(5)
'''
Calculating 5!
Calculating 4!
Calculating 3!
Calculating 2!
Calculating 1!
Out[82]: 120
'''
fact(5) #Out[83]: 120

fact(6) #Calculating 6!
#Out[84]: 720

'''
Our simple memoizer has a drawback however:

the cache size is unbounded - probably not a good thing! In general we want to limit the cache to a certain number of entries, balancing computational efficiency vs memory utilization.
we are not handling **kwargs
Memoization is such a common thing to do that Python actually has a memoization decorator built for us!

It's in the, you guessed it, functools module, and is called lru_cache and is going to be quite a bit more efficient compared to the rudimentary memoization example we did above.

[LRU Cache = Least Recently Used caching: since the cache is not unlimited, at some point cached entries need to be discarded, and the least recently used entries are discarded first]
'''

#In cases, the cache size may grow infinitely. So we use lru - default cache size is 128 and that can be overwritten 

from functools import lru_cache

@lru_cache()
def fact(n):
    print("Calculating fact({0})".format(n))
    return 1 if n < 2 else n * fact(n-1)

fact(5)
'''
Calculating fact(5)
Calculating fact(4)
Calculating fact(3)
Calculating fact(2)
Calculating fact(1)
Out[85]: 120
'''

fact(6)
'''
Calculating fact(6)
Out[86]: 720
'''
#One of the arguments to the lru_cache decorator is the size of the cache - it defaults to 128 items, but we can easily change this - for performance reasons use powers of 2 for the cache size (or None for unbounded cache):
    
@lru_cache(maxsize=8)
def fib(n):
    print("Calculating fib({0})".format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)


fib(10)
''''
Calculating fib(8)
Calculating fib(7)
Calculating fib(6)
Calculating fib(5)
Calculating fib(4)
Calculating fib(3)
Calculating fib(2)
Calculating fib(1)
Out[95]: 21
'''

fib(20)
'''
Calculating fib(20)
Calculating fib(19)
Calculating fib(18)
Calculating fib(17)
Calculating fib(16)
Calculating fib(15)
Calculating fib(14)
Calculating fib(13)
Calculating fib(12)
Calculating fib(11)
Out[96]: 6765
'''
#we have till fib(10) excluding fib(1) and fib(2) as the max size is 8.
#to calculate feb(20) we have to have values 19 and 18











