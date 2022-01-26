'''
What are Lambda Expressions?

We already know how to create functions using the def statement

Lambda expressions are simply another way to create functions -- anonymous functions


Syntax:
lambda [parameter list]: expression  --> the :is required, even for zero arguments
   |        |||           |||||
keyword parameter list this expression is evaluated and returned when the lambda function is called (think of it as the "body" of the function)
         (optional)


the expression returns a function object that evaluates and returns the expression when it is called

Function can be assigned to a variable or/and passed as an argument to another function
it is a function, just like one created with def

Examples

lambda x: x**2 
lambda x, y: x + y 
lambda : 'hello' 
lambda s: s[::-1].upper()

type(lambda x: x**2) →function

Note that these expressions are function objects, but are not "named" →anonymous functions

Lambdas, or anonymous functions, are NOT equivalent to closures

Assigning a Lambda to a Variable Name

my_func = lambda x: x**2 

my_func(3) →9
my_func(4) →16

type(my_func) → function

identical to:
def my_func(x):
    return x**2

my_func(3) →9
my_func(4) →16

type(my_func) → function

Passing as an Argument to another Function

def apply_func(x, fn):
    return fn(x)

apply_func(3, lambda x: x**2)              → 9

apply_func(2, lambda x: x + 5)             → 7

apply_func('abc', lambda x: x[1:] * 3)     → bcbcbc

equivalently:
def fn_1(x):
    return x[1:] * 3
apply_func('abc', fn_1) → bcbcbc
--------------------------------------------------------------------------------

Limitations
The "body" of a lambdais limited to a single expression

no assignments     lambda x: x = 5 lambda x: x = x + 5 both are not permitted

no annotations 

def func(x: int):
    return x**2 -- this can be done as it is a normal function.

But cannot be used in a lambda function.

lambda x:int : x*2    ---- Error

single logical line of code →line-continuation is OK, but still just one expression
lambda x: x * \
    math.sin(x)    ----- This is permitted
'''
lambda x: x**2 #<function __main__.<lambda>(x)>

#Assigning to a varible

func = lambda x: x**2
type(func) #function

func(2) #4

#we can assign the defaut values in lambda

func1 = lambda x,y=10: (x,y)
func1(1,2) #(1, 2)
func1(1) #(1, 10)

#we can use * and ** as well
func2 = lambda x, *args, **kwargs: (x,*args, {**kwargs})
a = func2(1, 'a', 'b', y=100, a=10, b=20) #(1, 'a', 'b', {'y': 100, 'a': 10, 'b': 20})

#passing lambda as an argument
def applyfunc(x,fn):
    return fn(x)
    
applyfunc(3, lambda x: x**2) #9

applyfunc(3, lambda x:x**3) #27

#more generic 

def applyfunc(fn,*args,**kwargs):
    return fn(*args,**kwargs)

applyfunc(lambda x,y:x+y,1,2) #3
applyfunc(lambda x,y:x+y,1,y=2) #3
applyfunc(lambda x:sum(x),[1,2,3,4,5]) #15
#or
applyfunc(sum,[1,2,3,4,5]) #15
