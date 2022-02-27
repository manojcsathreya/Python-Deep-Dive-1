'''
DECORATORS
---------------------------------------------------------------------------
Recall the simple closure example we did which allowed to us to maintain a 
count of how many times a function was called:

Decorators

def counter(fn):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print('Function {0} was called {1} times'.format(fn.__name__, count)
        return fn(*args, **kwargs)
    return inner


def add(a, b=0):
    return a + b
add = counter(add)
result = add(1, 2) →Function add was called 1 times
                   →result = 3
                   
                   
using *args, **kwargs means we can call
any function fnwith any combination of 
positional and keyword-only arguments
                   
We essentially modified our addfunction by wrapping it inside another 
function that added some functionality to it
We also say that we decorated our function add with the function counter
And we call counter a decorator function

---------------------------------------------------------------------------
Decorators
In general a decorator function:
• takes a function as an argument
• returns a closure
• the closure usually accepts any combination of parameters
• runs some code in the inner function (closure)
• the closure function calls the original function using the arguments passed to the closure
• returns whatever is returned by that function call

---------------------------------------------------------------------------
Decorators and the @Symbol
In our previous example, we saw that counter was a decorator
and we could decorate our addfunction using: add = counter(add)

In general, if funcis a decorator function, we decorate another function my_func using:
my_func = func(my_func)

This is so common that Python provides a convenient way of writing that:

@counter
def add(a, b):
    return a + b

is the same as writing is the same as writing

def add(a, b):
    return a + b
add = counter(add)

@func
def my_func(…):
…

is the same as writing is the same as writing

def my_func(…):
…
my_func = func(my_func)
---------------------------------------------------------------------------
Introspecting Decorated Functions
Let's use the same countdecorator.

def counter(fn):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print('{0} was called {1} times'.format(fn.__name__, count))
        return fn(*args, **kwargs)
    return inner

@counter 
def mult(a, b, c=1):
    """
        returns the product of three values
    """
    return a * b * c

remember we could equally have written:
mult = counter(mult)

mult.__name__ →inner <not mult>
mult's name "changed" when we decorated it
they are not the same function after all
help(mult) →Help on function inner in module __main__:
inner(*args, **kwargs)

We have also "lost" our docstring, 
and even the original function signature
Even using the inspect module's signature does not yield better results

---------------------------------------------------------------------------
One approach to fixing this

We could try to fix this problem, at least for the docstring and function name as follows:

def counter(fn):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print('Function {0} was called {1} times'.format(fn.__name__, count))
        return fn(*args, **kwargs)
        inner.__name__ = fn.__name__
        inner.__doc__ = fn.__doc__
    return inner

But this doesn’t fix losing the function signature – doing so would be quite complicated

Instead, Python provides us with a special function that we can use to fix this
---------------------------------------------------------------------------
The functools.wraps function

The functools module has a wraps function that we can use to fix the metadata of our inner
function in our decorator

In fact, the wrapsfunction is itself a decorator 

but it needs to know what was our "original" function – in this case fn

def counter(fn):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(count)
        return fn(*args, **kwargs)
    inner = wraps(fn)(inner)
    return inner


OR


from functools import wraps

def counter(fn):
    count = 0
    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(count)
        return fn(*args, **kwargs)
    return inner

---------------------------------------------------------------------------
def counter(fn):
    count = 0
    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(count)
        return fn(*args, **kwargs)
    return inner

@counter
def mult(a:int, b:int, c:int=1):
    """
    returns the product of three values
    """
    return a * b * c

help(mult) → Help on function mult in module __main__:
mult(a:int, b:int, c:int=1)
returns the product of three values

And introspection using the inspect module works as expected:
inspect.signature(mult) → <Signature (a:int, b:int, c:int=1)>

You don't have to use @wraps, but it will make debugging easier!

---------------------------------------------------------------------------


'''

def counter(fn):
    count = 0
    def inner(*args,**kwargs):
        nonlocal count
        count+=1
        print('function{0} was called {1} times'.format(fn.__name__,count))
        return fn(*args,**kwargs)
    
    return inner 

def add(a:int, b:int = 0):
    """
    Adds two numbers
    """
    return a+b

help(add)
'''
Help on function add in module __main__:

add(a: int, b: int = 0)
    Adds two numbers
'''
id(add) #1732170571840

#now we decorate the function by counter
add = counter(add)
id(add) #1732170534624
#you can see the id got changed. why? coz the id is of the inner function
help(add)
'''
Help on function inner in module __main__:

inner(*args, **kwargs)
'''
#we have lost all the documentations we had for our original add function.
#and add wrks just fine as it takes arbitrary number of arguments

add(10,20)
#functionadd was called 1 times 30

add(10)
#functionadd was called 2 times 10

#we'll also do the same thing to mult
@counter
def mult(a: float, b: float=1, c: float=1) -> float:
    """
    returns the product of a, b, and c
    """
    return a * b * c

help(mult)
'''
Help on function inner in module __main__:

inner(*args, **kwargs)
'''

#To fix the issue of documentation loss

def counter(fn):
    count = 0
    def inner(*args,**kwargs):
        '''
        This is an inner closure
        '''
        nonlocal count
        count+=1
        print('function{0} was called {1} times'.format(fn.__name__,count))
        return fn(*args,**kwargs)
    inner.__name__ = fn.__name__
    inner.__doc__ = fn.__doc__
    return inner 

@counter
def mult(a: float, b: float=1, c: float=1) -> float:
    """
    returns the product of a, b, and c
    """
    return a * b * c

help(mult)
'''

mult(*args, **kwargs)
    returns the product of a, b, and c
    
However, the params are of inner function

'''

from functools import wraps
#we have two ways of doing this
#Way 1
def counter(fn):
    count = 0
    @wraps(fn)
    def inner(*args,**kwargs):
        '''
        This is an inner closure
        '''
        nonlocal count
        count+=1
        print('function{0} was called {1} times'.format(fn.__name__,count))
        return fn(*args,**kwargs)
    
    return inner 

@counter
def mult(a: float, b: float=1, c: float=1) -> float:
    """
    returns the product of a, b, and c
    """
    return a * b * c

help(mult)

'''
Help on function mult in module __main__:

mult(a: float, b: float = 1, c: float = 1) -> float
    returns the product of a, b, and c
'''

#or
#WAY 2
def counter(fn):
    count = 0
    
    def inner(*args,**kwargs):
        '''
        This is an inner closure
        '''
        nonlocal count
        count+=1
        print('function{0} was called {1} times'.format(fn.__name__,count))
        return fn(*args,**kwargs)
        
    inner = wraps(fn) (inner)
    return inner 

@counter
def mult(a: float, b: float=1, c: float=1) -> float:
    """
    returns the product of a, b, and c
    """
    return a * b * c

help(mult)

'''
Help on function mult in module __main__:

mult(a: float, b: float = 1, c: float = 1) -> float
    returns the product of a, b, and c
'''
