#Closure application 2
#Example 1
#Let's write a small function that can increment a counter for us - we don't have an incrementor in Python (the ++ operator in Java or C++ for example):
    
def counter(initial_value):
    def inc(increment=1):
        nonlocal initial_value
        initial_value+=increment
        return initial_value
    return inc

counter1 = counter(0)
print(counter1()) #1
print(counter1()) #2
print(counter1()) #3
print(counter1()) #4

print(counter1(8)) #12

counter2 = counter(1000)
print(counter2(1)) #1001
print(counter2()) #1002
print(counter2(20)) #1022

#Example 2
#Let's modify this example to now build something that can run, and maintain a count of how many times we have run some function.

def counter(fn):
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt+=1
        print('{0} function has been called {1} times'.format(fn.__name__,cnt))
        return fn(*args,**kwargs)
    return inner 

def add(a,b):
    return a+b

counter_add = counter(add)
counter_add.__closure__
'''
(<cell at 0x0000022B52A99E50: int object at 0x00007FF973E92710>,
 <cell at 0x0000022B52A99B20: function object at 0x0000022B52B2ADC0>)
'''
counter_add.__code__.co_freevars #('cnt', 'fn')

counter_add(10,20)
# add function has been called 1 times 30

counter_add(1,2)
#add function has been called 2 times 3

counter_add(22, 33)
#add function has been called 3 times 55

def mult(a,b,c):
    return a*b*c

counter_mult = counter(mult)
counter_mult(2,3,4)
#mult function has been called 1 times 24

#Example 3
#Let's take this one step further, and actually store the function name and the number of calls in a global dictionary instead of just printing it out all the time.
counters = dict()
def counter(fn):
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt+=1
        counters[fn.__name__] = cnt #counters is global
        return fn(*args,**kwargs)
    return inner 

def add(a,b):
    return a+b

counted_add = counter(add)
counted_mult = counter(mult)

counted_add(10, 20) #30

counters #{'add': 1}

counted_add(50, 20) #70

counters #{'add': 2}

counted_mult(10, 20, 1) #200

counters #{'add': 2, 'mult': 1}

#Of course this relies on us creating the counters global variable first and making sure we are naming it that way, so instead, we're going to pass it as an argument to the counter function:

def counter(fn, counters):
    cnt = 0  # initially fn has been run zero times
    
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt = cnt + 1
        counters[fn.__name__] = cnt  # counters is nonlocal
        return fn(*args, **kwargs)
    
    return inner

func_counters = dict()
counted_add = counter(add, func_counters)
counted_mult = counter(mult, func_counters)

counted_add.__code__.co_freevars     # ('cnt', 'counters', 'fn')

for i in range(5):
    counted_add(i, i)

for i in range(10):
    counted_mult(i, i, i)
    
print(func_counters) #{'add': 5, 'mult': 10}

def fact(n):
    product = 1
    for i in range(2,n+1):
        product *=i
        
    return product

counted_fact = counter(fact,func_counters)
counted_fact(4) #24
func_counters #{'add': 5, 'mult': 10, 'fact': 1}

#Of course, we don't have to assign the "counted" version of our functions a new name - we can simply assign it to the same name!
fact = counter(fact, func_counters)
fact(3) #6
fact(4) #24
func_counters #{'add': 5, 'mult': 10, 'fact': 2}

#Notice, how we essentially added some functionality to our fact function, without modifying what the fact function actually returns.

#This leads us straight into our next topic: decorators!
