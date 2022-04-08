def func():
    a = 10
    return a

func #<function __main__.func()>
func() #10
id(func) #2399924491888
print(globals()) #tells us about the whole global name space

f = globals()['func']
f is func #True

locals() is globals() #True

def func():
    a=10
    b=10
    print(locals())
    
func() #{'a': 10, 'b': 10}

import math
import fractions

math # <module 'math' (built-in)>  -- #built-in

fractions #<module 'fractions' from 'C:\\Users\\Manoj.Sathish\\Anaconda3\\lib\\fractions.py'>  - #standard namespace

junk = globals()['math']

junk is math #True

id(math) #2399781516928
id(junk) #2399781516928

del math
math #name 'math' is not defined

junk #<module 'math' (built-in)>

import math

id(math) #2399781516928
# same as old ones
# so when modules are created it adds a reference not only in globals() but also in sys.cache()
#as long as you are using same virtual environment, from ehichever module you import, it is created only once

import sys
type(sys.modules) #dict

sys.modules['math'] #<module 'math' (built-in)>

sys.modules['junk'] #KeyError: 'junk'

math.__name__ #'math'

math.__dict__
'''
{'__name__': 'math',
 '__doc__': 'This module provides access to the mathematical functions\ndefined by the C standard.',
 '__package__': '',
 '__loader__': _frozen_importlib.BuiltinImporter,
 '__spec__': ModuleSpec(name='math', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in'),
 'acos': <function math.acos(x, /)>,
 'acosh': <function math.acosh(x, /)>,
 'asin': <function math.asin(x, /)>,
 'asinh': <function math.asinh(x, /)>,
 'atan': <function math.atan(x, /)>,
 'atan2': <function math.atan2(y, x, /)>,
 'atanh': <function math.atanh(x, /)>,
 'ceil': <function math.ceil(x, /)>,
 'copysign': <function math.copysign(x, y, /)>,
 'cos': <function math.cos(x, /)>,
 'cosh': <function math.cosh(x, /)>,
 'degrees': <function math.degrees(x, /)>,
 'dist': <function math.dist(p, q, /)>,
 'erf': <function math.erf(x, /)>,
 'erfc': <function math.erfc(x, /)>,
 'exp': <function math.exp(x, /)>,
 'expm1': <function math.expm1(x, /)>,
 'fabs': <function math.fabs(x, /)>,
 'factorial': <function math.factorial(x, /)>,
 'floor': <function math.floor(x, /)>,
 'fmod': <function math.fmod(x, y, /)>,
 'frexp': <function math.frexp(x, /)>,
 'fsum': <function math.fsum(seq, /)>,
 'gamma': <function math.gamma(x, /)>,
 'gcd': <function math.gcd(x, y, /)>,
 'hypot': <function math.hypot>,
 'isclose': <function math.isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)>,
 'isfinite': <function math.isfinite(x, /)>,
 'isinf': <function math.isinf(x, /)>,
 'isnan': <function math.isnan(x, /)>,
 'isqrt': <function math.isqrt(n, /)>,
 'ldexp': <function math.ldexp(x, i, /)>,
 'lgamma': <function math.lgamma(x, /)>,
 'log': <function math.log>,
 'log1p': <function math.log1p(x, /)>,
 'log10': <function math.log10(x, /)>,
 'log2': <function math.log2(x, /)>,
 'modf': <function math.modf(x, /)>,
 'pow': <function math.pow(x, y, /)>,
 'radians': <function math.radians(x, /)>,
 'remainder': <function math.remainder(x, y, /)>,
 'sin': <function math.sin(x, /)>,
 'sinh': <function math.sinh(x, /)>,
 'sqrt': <function math.sqrt(x, /)>,
 'tan': <function math.tan(x, /)>,
 'tanh': <function math.tanh(x, /)>,
 'trunc': <function math.trunc(x, /)>,
 'prod': <function math.prod(iterable, /, *, start=1)>,
 'perm': <function math.perm(n, k=None, /)>,
 'comb': <function math.comb(n, k, /)>,
 'pi': 3.141592653589793,
 'e': 2.718281828459045,
 'tau': 6.283185307179586,
 'inf': inf,
 'nan': nan}
'''

sqrt = math.__dict__['sqrt']
sqrt(4) #2.0

# till now, we know modules are of certain data type, it is loaded from somewehere else. Usually from files
#contains their own globals 

#Module data types
import fractions

from types import ModuleType

isinstance(fractions, ModuleType) #True

#to create module types

#new modulename  = ModuleType('Name of the module','additional doc strings')

mod = ModuleType('mod','This is a test module')
mod.__dict__
'''
{'__name__': 'mod',
 '__doc__': 'This is a test module',
 '__package__': None,
 '__loader__': None,
 '__spec__': None}
'''
mod.pi = 3.14
mod.__dict__
'''
{'__name__': 'mod',
 '__doc__': 'This is a test module',
 '__package__': None,
 '__loader__': None,
 '__spec__': None,
 'pi': 3.14}
'''
    
mod.hello = lambda: 'Hello!'
mod.__dict__
'''
{'__name__': 'mod',
 '__doc__': 'This is a test module',
 '__package__': None,
 '__loader__': None,
 '__spec__': None,
 'pi': 3.14,
 'hello': <function __main__.<lambda>()>}
'''
mod.hello() #'Hello!'

'mod' in globals() #True
'hello' in globals() #Flase
hello = mod.hello
'hello' in globals() #True

hello() #'Hello!'

from collections import namedtuple

mod.Point = namedtuple('Point', 'x y')
p1= mod.Point(0,0)
p2 = mod.Point(10,20)
p1 #Point(x=0, y=0)
