def logged(fn):
    from functools import wraps
    from datetime import datetime, timezone
    
    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt = datetime.now(timezone.utc)
        result = fn(*args, **kwargs)
        print('{0}: called {1}'.format(fn.__name__, run_dt))
        return result
        
    return inner

@logged
def func_1():
    pass

@logged
def func_2():
    pass

func_1() #func_1: called 2022-03-01 03:01:14.126737+00:00

func_2() #func_2: called 2022-03-01 03:01:28.307788+00:00

#we take timer function for prev tutorial
def timed(fn):
    from functools import wraps
    from time import perf_counter
    
    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        print('{0} ran for {1:.6f}s'.format(fn.__name__, end-start))
        return result
    
    return inner

@timed
@logged
def factorial(n):
    from operator import mul
    from functools import reduce
    
    return reduce(mul, range(1, n+1))

factorial(3)
#factorial: called 2022-03-01 03:03:41.229873+00:00
#factorial ran for 0.001590s

#well it is the same thing as 
factorial = logged(timed(factorial))


#you can see the decorated functions are stacked and are called on the basis of their order

#to understand it more further

def dec_1(fn):
    def inner():
        print('Running Dec1')
        return fn()
    return inner

def dec_2(fn):
    def inner():
        print('Running Dec2')
        return fn()
    return inner

@dec_1 
@dec_2 
def myfunc():
    print('Running my func')
    

myfunc()
'''
Running Dec1
Running Dec2
Running my func
'''
#What is happening here is dec_1 is called first because of the order and dec1 encounter 
# print functio and then it calles dec 2

#if we do the reverse

def dec_1(fn):
    def inner():
        res = fn()
        print('Running Dec1')
        return res
    return inner

def dec_2(fn):
    def inner():
        res = fn()
        print('Running Dec2')
        return res
    return inner

@dec_1 
@dec_2 
def myfunc():
    print('Running my func')
    

myfunc()
'''
Running my func
Running Dec2
Running Dec1
'''



def dec_1(fn):
    def inner():
        res = fn()
        print('Running Dec1')
        return res
    return inner

def dec_2(fn):
    def inner():
        res = fn()
        print('Running Dec2')
        return res
    return inner

@dec_1 
@dec_2 
@dec_1 
@dec_2 
def myfunc():
    print('Running my func')
    

myfunc()
'''
Running my func
Running Dec2
Running Dec1
Running Dec2
Running Dec1
'''






