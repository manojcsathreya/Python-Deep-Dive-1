'''
Functions are first-class objects

Functions have attributes   __doc__    and     __annotations__

We can attach our own attributes

def my_func(a, b):
    return a + b

my_func.category = 'math'
my_func.sub_category = 'arithmetic'

print(my_func.category) →math
print(my_func.sub_category) →arithmetic


-------------------------------------------------------------------------------------------
The dir()function

dir()is a built-in function that, given an object as an argument, will return a list of valid 
attributes for that object

dir(my_func)

['__annotations__', '__call__', '__class__', '__closure__', 
'__code__', '__defaults__', '__delattr__', '__dict__',
'__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
'__get__', '__getattribute__', '__globals__', '__gt__',
'__hash__', '__init__', '__init_subclass__', '__kwdefaults__', 
'__le__', '__lt__', '__module__', '__name__',
'__ne__', '__new__', '__qualname__', '__reduce__', 
'__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
'__str__', '__subclasshook__', 'category', 'sub_category']

-------------------------------------------------------------------------------------------

Function Attributes: __name__, __defaults__, __kwdefaults__

__name__ →name of function
__defaults__ →tuple containing positional parameter defaults
__kwdefaults__ →dictionary containing keyword-only parameter defaults

def my_func(a, b=2, c=3, *, kw1, kw2=2):
pass

my_func.__name__ → my_func

my_func.__defaults__ → (2, 3)

my_func.__kwdefaults__ → {'kw2': 2}

-------------------------------------------------------------------------------------------
Function Attribute: __code__

def my_func(a, b=1, *args, **kwargs):
i = 10
b = min(i, b)
return a * b

my_func.__code__
→ <code object my_func at 0x00020EEF … >

This __code__ object itself has various properties, which include:

co_varnames parameter and local variables
my_func.__code__.co_varnames → ('a', 'b', 'args', 'kwargs', 'i')
parameter names first, followed by local variable names

co_argcount number of parameters
my_func.__code__.co_argcount → 2
does not count *argsand **kwargs!

-------------------------------------------------------------------------------------------

The inspect Module 

import inspect
ismethod(obj) isfunction(obj) isroutine(obj) and many others…

What's the difference between a function and a method?
Classes and objects have attributes – an object that is bound (to the class or the object)

def my_func():
pass
def MyClass:
def func(self):
pass
my_obj = MyClass()

ismethod(my_func) → False

isfunction(my_func) → True

ismethod(my_obj.func) → True

isfunction(my_obj.func) → False

An attribute that is callable, is called a method
funcis bound to my_obj, an instance of MyClass

isroutine(my_func) → True
isroutine(my_obj.func) → True

'''
def fact(n: "some non-negative integer") -> "n! or 0 if n < 0":
    """Calculates the factorial of a non-negative integer n
    
    If n is negative, returns 0.
    """
    if n < 0:
        return 0
    elif n <= 1:
        return 1
    else:
        return n * fact(n-1)
    
fact.short_description = "factorial function"
print(fact.short_description) #factorial function

fact.__doc__ #'Calculates the factorial of a non-negative integer n\n    \n    If n is negative, returns 0.\n    '

fact.__annotations__ #{'n': 'some non-negative integer', 'return': 'n! or 0 if n < 0'}

def my_func(a, b=2, c=3, *, kw1, kw2=2, **kwargs):
    pass

f = my_func

my_func.__name__ #'my_func'

f.__name__ #'my_func'

my_func.__defaults__ #(2, 3)

my_func.__kwdefaults__ #{'kw2': 2}

def my_func(a, b=1, *args, **kwargs):
    i = 10
    b = min(i, b)
    return a * b

my_func('a', 100) #'aaaaaaaaaa'

dir(my_func.__code__)
'''
['__class__',
 '__delattr__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 'co_argcount',
 'co_cellvars',
 'co_code',
 'co_consts',
 'co_filename',
 'co_firstlineno',
 'co_flags',
 'co_freevars',
 'co_kwonlyargcount',
 'co_lnotab',
 'co_name',
 'co_names',
 'co_nlocals',
 'co_posonlyargcount',
 'co_stacksize',
 'co_varnames',
 'replace']
'''

#The code attribute contains a code object:
my_func.__code__ #<code object my_func at 0x0000016640E71300, file "<ipython-input-13-785cf1a800f4>", line 1>

#Attribute co_varnames is a tuple containing the parameter names and local variables:
my_func.__code__.co_varnames #('a', 'b', 'args', 'kwargs', 'i')

#Attribute co_argcount returns the number of arguments (minus any * and ** args)
my_func.__code__.co_argcount

#The inspect module. It is much easier to use the inspect module!
import inspect
inspect.isfunction(my_func) #True

inspect.ismethod(my_func) #False

class MyClass:
    def f_instance(self):
        pass
    
    @classmethod
    def f_class(cls):
        pass
    
    @staticmethod
    def f_static():
        pass
    
#Instance methods are bound to the instance of a class (not the class itself)

#Class methods are bound to the class, not instances

#Static methods are no bound either to the class or its instances

inspect.isfunction(MyClass.f_instance), inspect.ismethod(MyClass.f_instance) #(True, False)

inspect.isfunction(MyClass.f_class), inspect.ismethod(MyClass.f_class) #(False, True)

inspect.isfunction(MyClass.f_static), inspect.ismethod(MyClass.f_static) #(True, False)

my_obj = MyClass()

inspect.isfunction(my_obj.f_instance), inspect.ismethod(my_obj.f_instance)  #(False, True)
inspect.isfunction(my_obj.f_class), inspect.ismethod(my_obj.f_class) #(False, True)a
inspect.isfunction(my_obj.f_static), inspect.ismethod(my_obj.f_static) #(True, False)
