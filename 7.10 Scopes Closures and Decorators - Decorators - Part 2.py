'''
DECORATORS -- 2

Decorator Parameters

In the previous videos we saw some built-in decorators that can handle some arguments:

@wraps(fn)
def inner():
…


EX:
@lru_cache(maxsize=256)  --- function cal
def factorial(n):
…

This should look quite different from the decorators we have been creating and using:
@timed                  --- no function call
def fibonacci(n):
…

The old timed decorator
def timed(fn):
    from time import perf_counter
    def inner(*args, **kwargs):
        total_elapsed = 0
        for i in range(10):                              ----> hardcoded value 10
            start = perf_counter()
            result = fn(*args, **kwargs)
            total_elapsed += (perf_counter() - start)
            avg_elapsed = total_elapsed / 10
            print(avg_elapsed)
        return result
    return inner

@timed
def my_func():
…

OR my_func = timed(my_func)
------------------------------------------------------------------------------------
One Approach
def timed(fn, reps):   --> Reps is an extra parameter
    from time import perf_counter
    def inner(*args, **kwargs):
        total_elapsed = 0
        for i in range(reps):      ---> reps is a free variable
            start = perf_counter()
            result = fn(*args, **kwargs)
            total_elapsed += (perf_counter() - start)
            avg_elapsed = total_elapsed / reps
            print(avg_elapsed)
        return result
    return inner

We can do
my_func = timed(my_func, 10)

but we cannot do
@timed(10)
def my_func():
------------------------------------------------------------------------------------
Rethinking the solution
@timed
def my_func():
    …
OR
my_func = timed(my_func)

So, timed is a function that returns that inner closure that contains our original function

In order for this to work as intended:
@timed(10)
def my_func():
…
timed(10) will need to return our original timed decorator when called

dec = timed(10)  -- timed(10) returns a decorator
@dec             -- and we decorate our function with dec
def my_func():
…
------------------------------------------------------------------------------

Nested closures to the rescue!

def outer(reps):
    def timed(fn):
        from time import perf_counter
        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(reps):                         -- free variable bound to reps in outer
                start = perf_counter()
                result = fn(*args, **kwargs)
                total_elapsed += (perf_counter() - start)
                avg_elapsed = total_elapsed / reps
                print(avg_elapsed)
            return result
        return inner
    return timed                                     --- calling outer(n) returns our original decorator <with reps set to n(free variable)>


@outer(10)
def my_func():
…
 OR

my_func = outer(10)(my_func)
--------------------------------------------------------------------------------------------------------------
Decorator Factories

The outerfunction is not itself a decorator instead it returns a decorator when called

and any arguments passed to outercan be referenced (as free variables) inside our decorator

We call this outer function a decorator factory function
(it is a function that creates a new decorator each time it is called)
----------------------------------------------------------------------------------------------------------------
And finally…

To wrap things up, we probably don't want out decorator call to look like:
@outer(10)
def my_func():
…

It would make more sense to write it this way:
@timed(10)
def my_func():
…

All we need to do is change the names of the outerand timed functions

def timed(reps):                            ------this was outer
    def dec(fn):                             ------this was timed
        from time import perf_counter

        @wraps(fn)                          --------we can still use @wraps
        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                total_elapsed += (perf_counter() - start)
                avg_elapsed = total_elapsed / reps
                print(avg_elapsed)
            return result
        return inner
    return dec


@timed(10)
def my_func():
…

'''

def timed(fn):
    from time import perf_counter
    print('Running timed')
    def inner(*args,**kwargs):
        print('Running inner')
        start = perf_counter()
        result = fn(*args,**kwargs)
        end = perf_counter()
        print('Run time: {0:.6f}s elapsed'.format(end-start))
        return result
    return inner

def calc_fib(n):
    return 1 if n<=2 else calc_fib(n-1)+calc_fib(n-2)

@timed
def fib(n):
    return calc_fib(n)    
    
fib(10)
'''
Running timed
Running inner
Run time: 0.000039s elapsed
Out[2]: 55
'''

#Let's modify this so the timer runs the function multiple times and calculates the average run time:
    
def timed(fn):
    from time import perf_counter
    print('Running timed')
    
    def inner(*args,**kwargs):
        elapsed_time = 0
        print('Running inner')
        for i in range(10):
            start = perf_counter()
            result = fn(*args,**kwargs)
            end = perf_counter()
            elapsed_time+=(end-start)
        print('Run time: {0:.6f}s elapsed '.format((elapsed_time/10)))
        return result
    return inner
    
def calc_fib(n):
    return 1 if n<=2 else calc_fib(n-1)+calc_fib(n-2)

@timed
def fib(n):
    return calc_fib(n) 

fib(28)
'''
Running inner
Run time: 0.137006s elapsed 
Out[8]: 317811
'''

#But that value of 10 has been hardcoded. Let's make it a parameter instead.
    
def timed(fn,reps):
    from time import perf_counter
    print('Running timed')
    
    def inner(*args,**kwargs):
        elapsed_time = 0
        print('Running inner')
        for i in range(reps):
            start = perf_counter()
            result = fn(*args,**kwargs)
            end = perf_counter()
            elapsed_time+=(end-start)
        print('Run time: {0:.6f}s elapsed ({1} reps)'.format((elapsed_time/reps),reps))
        return result
    return inner
    
def calc_fib(n):
    return 1 if n<=2 else calc_fib(n-1)+calc_fib(n-2)

def fib(n):
    return calc_fib(n) 
    
fib = timed(fib,20)

fib(28)
'''
Running inner
Run time: 0.145263s elapsed (20 reps)
Out[13]: 317811
'''
    
'''
The problem is that we cannot use the @ decorator syntax because when using that syntax Python passes a single argument to the decorator: the function we are decorating - nothing else.

Of course we could just use what we did above, but the decorator syntax is kind of neat, so it would be nice to retain the ability to use it.

We just need to change our thinking a little bit to do this:

First, when we see the following syntax:

@dec
def my_func():
    pass

we see that dec must be a function that takes a single argument, the function being decorated.

You'll note that dec is just a function, but we do not call dec when we decorate my_func, we simply use the label dec.

Then Python does:

my_func = dec(my_func)

Let's try a concrete example:
'''

def dec(fn):
    print('Running dec')
    
    def inner(*args,**kwargs):
        print('Running inner')
        return fn(*args,**kwargs)
    
    return inner 

def my_func():
    print('Running my_func')
    
#decoratinf my_func with dec
my_func = dec(my_func)#Running dec
#we are now calling dec so it is printing ''Running dec''

my_func()
'''
Running inner
Running my_func
'''
'''
But what if dec was not the decorator itself, but instead created and returned a decorator?

Let's see how we might do this:
'''

def dec_factory():
    print('Running dec factory')
    def dec(fn):
        print('Running dec')
    
        def inner(*args,**kwargs):
            print('Running inner')
            return fn(*args,**kwargs)
    
        return inner 
    return dec 

def my_func():
    print('Running my_func')
    
my_func = dec_factory()(my_func)
'''
Running dec factory
Running dec
'''

my_func()
'''
Running inner
Running my_func
'''

def timed_factory(num_reps=1):
    def timed(fn):
        from time import perf_counter

        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(num_reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                total_elapsed += (perf_counter() - start)
            avg_elapsed = total_elapsed / num_reps
            print('Avg Run time: {0:.6f}s ({1} reps)'.format(avg_elapsed,
                                                            num_reps))
            return result
        return inner
    return timed    

@timed_factory(5)
def fib(n):
    return calc_fib(n)

fib(30)

'''
Avg Run time: 0.395977s (5 reps)
Out[22]: 832040
'''

#Just to put the finishing touch on this, we probably don't want to have our outer function named the way it is (timed_factory). Instead we probably just want to call it timed. So lets just do this final part:
    
from functools import wraps

def timed(num_reps=1):
    def decorator(fn):
        from time import perf_counter

        @wraps(fn)
        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(num_reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                total_elapsed += (perf_counter() - start)
            avg_elapsed = total_elapsed / num_reps
            print('Avg Run time: {0:.6f}s ({1} reps)'.format(avg_elapsed,
                                                            num_reps))
            return result
        return inner
    return decorator  

@timed(5)
def fib(n):
    return calc_fib(n)


fib(30)
'''
Avg Run time: 0.253744s (5 reps)
832040
'''
