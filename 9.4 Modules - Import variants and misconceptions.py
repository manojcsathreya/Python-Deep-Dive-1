'''
Import variants
# module1.py
import math
is mathin sys.modules?
if not, load it and insert ref

sys.modules
math <module object>

add symbol mathto module1's global namespace referencing the same object

module1.globals()
math <module object>

mathsymbol in namespace

(if mathsymbol already exists in module1's namespace, replace reference)

# module1.py

import math as r_math

is math in sys.modules? if not, load it and insert ref

sys.modules
math <module object>

add symbol r_mathto module1's global namespace referencing the same object

module1.globals()
r_math <module object>

mathsymbol not in namespace

r_mathsymbol in namespace
(if r_mathsymbol already exists in module1's namespace, replace reference)


# module1.py
from math import sqrt

is mathin sys.modules?  if not, load it and insert ref

sys.modules

math <module object>

add symbol sqrtto module1's global namespace referencing math.sqrt

module1.globals()
sqrt <math.sqrt object>

(if sqrtsymbol already exists in module1's namespace, replace reference)

math symbol not in namespace


# module1.py

from math import sqrt as r_sqrt

is mathin sys.modules? if not, load it and insert ref

sys.modules
math <module object>

add symbol r_sqrtto module1's global namespace referencing math.sqrt

module1.globals()
r_sqrt <math.sqrt object>

(if r_sqrtsymbol already exists in module1's namespace, replace reference)

mathsymbol not in namespace


# module1.py
from math import *

is mathin sys.modules? if not, load it and insert ref

sys.modules
math <module object>

add "all" symbols defined in math to module1's global namespace
module1.globals()
pi <math.pi object>
sin <math.sin object>
and many more… mathsymbol not in namespace

(if any symbols already exists in module1's namespace, replace their reference)

what "all" means can be 
defined by the module being 
imported


Commonality

In every case the mathmodule was loaded into memory and referenced in sys.modules

Running from math import sqrt

did not "partially" load math

it only affected what symbols were placed in module1's namespace!

Things may be different with packages, but for simple modules this is the behavior


Why from <module> import *can lead to bugs

from cmath import *

# module1.py module1.globals()
sqrt <cmath.sqrt>
…

from math import * module1.globals()
sqrt <math.sqrt>
…
Overwriting

Efficiency

What's more efficient?

import math
or from math import sqrt

importing →same amount of work

calling math.sqrt(2)

sqrt(2)

This first needs to find the sqrtsymbol in math's namespace
dictlookup →super fast!

'''

#CODEE

import sys
'cmath' in sys.modules #flasr

'cmath' in globals() #False
from cmath import exp
 
'cmath' in globals() #flase
'exp' in globals()#true
 
'cmath' in sys.modules #true

from cmath import exp
'cmath' in globals() #False

'cmath' in sys.modules#True

'exp' in globals()#True

cmath = sys.modules['cmath']

from cmath import *
globals()
'''
{'__name__': '__main__',
 '__doc__': 'Automatically created module for IPython interactive environment',
 '__package__': None,
 '__loader__': None,
 '__spec__': None,
 '__builtin__': <module 'builtins' (built-in)>,
 '__builtins__': <module 'builtins' (built-in)>,
 '_ih': ['',
  'import sys',
  "'cmath' in sys.modules",
  'from cmath import exp',
  "'exp' in sys",
  'from cmath import exp',
  "'cmath' in globals()",
  "'cmath' in sys.modules",
  "'exp' in globals()",
  "cmath = sys.modules['cmath']",
  'del cmath',
  "'cmath' in globals() #False",
  'from cmath import exp',
  'cmath.sin(60)',
  'from cmath import *',
  'globals()'],
 '_oh': {2: True, 6: False, 7: True, 8: True, 11: False},
 '_dh': ['C:\\Users\\Manoj.Sathish'],
 'In': ['',
  'import sys',
  "'cmath' in sys.modules",
  'from cmath import exp',
  "'exp' in sys",
  'from cmath import exp',
  "'cmath' in globals()",
  "'cmath' in sys.modules",
  "'exp' in globals()",
  "cmath = sys.modules['cmath']",
  'del cmath',
  "'cmath' in globals() #False",
  'from cmath import exp',
  'cmath.sin(60)',
  'from cmath import *',
  'globals()'],
 'Out': {2: True, 6: False, 7: True, 8: True, 11: False},
 'get_ipython': <bound method InteractiveShell.get_ipython of <spyder_kernels.console.kernel.SpyderShell object at 0x0000020A407E9EE0>>,
 'exit': <IPython.core.autocall.ZMQExitAutocall at 0x20a408cc8e0>,
 'quit': <IPython.core.autocall.ZMQExitAutocall at 0x20a408cc8e0>,
 '_': False,
 '__': True,
 '___': True,
 '_i': 'from cmath import *',
 '_ii': 'cmath.sin(60)',
 '_iii': 'from cmath import exp',
 '_i1': 'import sys',
 'sys': <module 'sys' (built-in)>,
 '_i2': "'cmath' in sys.modules",
 '_2': True,
 '_i3': 'from cmath import exp',
 'exp': <function cmath.exp(z, /)>,
 '_i4': "'exp' in sys",
 '_i5': 'from cmath import exp',
 '_i6': "'cmath' in globals()",
 '_6': False,
 '_i7': "'cmath' in sys.modules",
 '_7': True,
 '_i8': "'exp' in globals()",
 '_8': True,
 '_i9': "cmath = sys.modules['cmath']",
 '_i10': 'del cmath',
 '_i11': "'cmath' in globals() #False",
 '_11': False,
 '_i12': 'from cmath import exp',
 '_i13': 'cmath.sin(60)',
 '_i14': 'from cmath import *',
 'acos': <function cmath.acos(z, /)>,
 'acosh': <function cmath.acosh(z, /)>,
 'asin': <function cmath.asin(z, /)>,
 'asinh': <function cmath.asinh(z, /)>,
 'atan': <function cmath.atan(z, /)>,
 'atanh': <function cmath.atanh(z, /)>,
 'cos': <function cmath.cos(z, /)>,
 'cosh': <function cmath.cosh(z, /)>,
 'isclose': <function cmath.isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)>,
 'isfinite': <function cmath.isfinite(z, /)>,
 'isinf': <function cmath.isinf(z, /)>,
 'isnan': <function cmath.isnan(z, /)>,
 'log': <function cmath.log>,
 'log10': <function cmath.log10(z, /)>,
 'phase': <function cmath.phase(z, /)>,
 'polar': <function cmath.polar(z, /)>,
 'rect': <function cmath.rect(r, phi, /)>,
 'sin': <function cmath.sin(z, /)>,
 'sinh': <function cmath.sinh(z, /)>,
 'sqrt': <function cmath.sqrt(z, /)>,
 'tan': <function cmath.tan(z, /)>,
 'tanh': <function cmath.tanh(z, /)>,
 'pi': 3.141592653589793,
 'e': 2.718281828459045,
 'tau': 6.283185307179586,
 'inf': inf,
 'infj': infj,
 'nan': nan,
 'nanj': nanj,
 '_i15': 'globals()'}
'''
#we can see sin and cos here. now lets import math module

from math import *
globals()
'''
{'__name__': '__main__',
 '__doc__': 'Automatically created module for IPython interactive environment',
 '__package__': None,
 '__loader__': None,
 '__spec__': None,
 '__builtin__': <module 'builtins' (built-in)>,
 '__builtins__': <module 'builtins' (built-in)>,
 '_ih': ['',
  'import sys',
  "'cmath' in sys.modules",
  'from cmath import exp',
  "'exp' in sys",
  'from cmath import exp',
  "'cmath' in globals()",
  "'cmath' in sys.modules",
  "'exp' in globals()",
  "cmath = sys.modules['cmath']",
  'del cmath',
  "'cmath' in globals() #False",
  'from cmath import exp',
  'cmath.sin(60)',
  'from cmath import *',
  'globals()',
  'from math import *',
  'globals()'],
 '_oh': {2: True, 6: False, 7: True, 8: True, 11: False, 15: {...}},
 '_dh': ['C:\\Users\\Manoj.Sathish'],
 'In': ['',
  'import sys',
  "'cmath' in sys.modules",
  'from cmath import exp',
  "'exp' in sys",
  'from cmath import exp',
  "'cmath' in globals()",
  "'cmath' in sys.modules",
  "'exp' in globals()",
  "cmath = sys.modules['cmath']",
  'del cmath',
  "'cmath' in globals() #False",
  'from cmath import exp',
  'cmath.sin(60)',
  'from cmath import *',
  'globals()',
  'from math import *',
  'globals()'],
 'Out': {2: True, 6: False, 7: True, 8: True, 11: False, 15: {...}},
 'get_ipython': <bound method InteractiveShell.get_ipython of <spyder_kernels.console.kernel.SpyderShell object at 0x0000020A407E9EE0>>,
 'exit': <IPython.core.autocall.ZMQExitAutocall at 0x20a408cc8e0>,
 'quit': <IPython.core.autocall.ZMQExitAutocall at 0x20a408cc8e0>,
 '_': {...},
 '__': False,
 '___': True,
 '_i': '\r\nfrom math import *',
 '_ii': 'globals()',
 '_iii': 'from cmath import *',
 '_i1': 'import sys',
 'sys': <module 'sys' (built-in)>,
 '_i2': "'cmath' in sys.modules",
 '_2': True,
 '_i3': 'from cmath import exp',
 'exp': <function math.exp(x, /)>,
 '_i4': "'exp' in sys",
 '_i5': 'from cmath import exp',
 '_i6': "'cmath' in globals()",
 '_6': False,
 '_i7': "'cmath' in sys.modules",
 '_7': True,
 '_i8': "'exp' in globals()",
 '_8': True,
 '_i9': "cmath = sys.modules['cmath']",
 '_i10': 'del cmath',
 '_i11': "'cmath' in globals() #False",
 '_11': False,
 '_i12': 'from cmath import exp',
 '_i13': 'cmath.sin(60)',
 '_i14': 'from cmath import *',
 'acos': <function math.acos(x, /)>,
 'acosh': <function math.acosh(x, /)>,
 'asin': <function math.asin(x, /)>,
 'asinh': <function math.asinh(x, /)>,
 'atan': <function math.atan(x, /)>,
 'atanh': <function math.atanh(x, /)>,
 'cos': <function math.cos(x, /)>,
 'cosh': <function math.cosh(x, /)>,
 'isclose': <function math.isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)>,
 'isfinite': <function math.isfinite(x, /)>,
 'isinf': <function math.isinf(x, /)>,
 'isnan': <function math.isnan(x, /)>,
 'log': <function math.log>,
 'log10': <function math.log10(x, /)>,
 'phase': <function cmath.phase(z, /)>,
 'polar': <function cmath.polar(z, /)>,
 'rect': <function cmath.rect(r, phi, /)>,
 'sin': <function math.sin(x, /)>,
 'sinh': <function math.sinh(x, /)>,
 'sqrt': <function math.sqrt(x, /)>,
 'tan': <function math.tan(x, /)>,
 'tanh': <function math.tanh(x, /)>,
 'pi': 3.141592653589793,
 'e': 2.718281828459045,
 'tau': 6.283185307179586,
 'inf': inf,
 'infj': infj,
 'nan': nan,
 'nanj': nanj,
 '_i15': 'globals()',
 '_15': {...},
 '_i16': '\r\nfrom math import *',
 'atan2': <function math.atan2(y, x, /)>,
 'ceil': <function math.ceil(x, /)>,
 'copysign': <function math.copysign(x, y, /)>,
 'degrees': <function math.degrees(x, /)>,
 'dist': <function math.dist(p, q, /)>,
 'erf': <function math.erf(x, /)>,
 'erfc': <function math.erfc(x, /)>,
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
 'isqrt': <function math.isqrt(n, /)>,
 'ldexp': <function math.ldexp(x, i, /)>,
 'lgamma': <function math.lgamma(x, /)>,
 'log1p': <function math.log1p(x, /)>,
 'log2': <function math.log2(x, /)>,
 'modf': <function math.modf(x, /)>,
 'pow': <function math.pow(x, y, /)>,
 'radians': <function math.radians(x, /)>,
 'remainder': <function math.remainder(x, y, /)>,
 'trunc': <function math.trunc(x, /)>,
 'prod': <function math.prod(iterable, /, *, start=1)>,
 'perm': <function math.perm(n, k=None, /)>,
 'comb': <function math.comb(n, k, /)>,
 '_i17': 'globals()'}
'''

#now we can see that math sin has replaced cmath sin


##EFFICIENCY
def my_func(a):
    import math
    return math.sqrt(a)

from time import perf_counter
from collections import namedtuple
Timings = namedtuple('Timings', 'timing_1 timing_2 abs_diff rel_diff')

def compare_timings(timing1,timing2):
    rel_diff = (timing2-timing1)/timing1 *100
     
    timings = Timings(round(timing1, 1),
                     round(timing2, 1),
                     round(timing2 - timing1, 2),
                     round(rel_diff, 2))
    return timings

test_repeats = 10_000_000

import math

start = perf_counter()
for _ in range(test_repeats):
    math.sqrt(2)
end = perf_counter()
elapsed_fully_qualified = end - start
print(f'Elapsed: {elapsed_fully_qualified}')
#Elapsed: 2.057656398357829

#Timing using a directly imported symbol name:
from math import sqrt

start = perf_counter()
for _ in range(test_repeats):
    sqrt(2)
end = perf_counter()
elapsed_direct_symbol = end - start
print(f'Elapsed: {elapsed_direct_symbol}')
#Elapsed: 1.603430354697538
compare_timings(elapsed_fully_qualified, elapsed_direct_symbol)
#Timings(timing_1=2.1, timing_2=1.6, abs_diff=-0.45, rel_diff_perc=-22.07)
#Definitely faster - but in absolute terms I really did not save a whole lot - over 10,000,000 iterations!

#Timing using a function (fully qualified symbol)
def func():
    math.sqrt(2)
    
start = perf_counter()
for _ in range(test_repeats):
    func()
end = perf_counter()
elapsed_func_fully_qualified = end - start
print(f'Elapsed: {elapsed_func_fully_qualified}') 
#Elapsed: 3.2668947610088703
compare_timings(elapsed_fully_qualified, elapsed_func_fully_qualified)
#Timings(timing_1=2.1, timing_2=3.3, abs_diff=1.21, rel_diff_perc=58.77)
#That was slower because of the function call overhead, but not by much in absolute terms considering I called func() 10,000,000 times!

#Timing using a function (direct symbol)
from math import sqrt
​
def func():
    sqrt(2)
    
start = perf_counter()
for _ in range(test_repeats):
    func()
end = perf_counter()
elapsed_func_direct_symbol = end - start
print(f'Elapsed: {elapsed_func_direct_symbol}')
#Elapsed: 2.80123663975316
compare_timings(elapsed_func_fully_qualified, elapsed_func_direct_symbol)
#Timings(timing_1=3.3, timing_2=2.8, abs_diff=-0.47, rel_diff_perc=-14.25)
#Slower, but again not by much in absolute terms considering this was for 10,000,000 iterations.

#Timing using a nested import (fully qualified symbol)
def func():
    import math
    math.sqrt(2)
    
start = perf_counter()
for _ in range(test_repeats):
    func()
end = perf_counter()
elapsed_nested_fully_qualified = end - start
print(f'Elapsed: {elapsed_nested_fully_qualified}')
#Elapsed: 5.041648347331877
compare_timings(elapsed_func_fully_qualified, elapsed_nested_fully_qualified)
#Timings(timing_1=3.3, timing_2=5.0, abs_diff=1.77, rel_diff_perc=54.33)
#So definitely slower. But in absolute terms, for 10,000,000 iterations?

#Timing using a nested import (direct symbol)
def func():
    from math import sqrt
    sqrt(2)
    
start = perf_counter()
for _ in range(test_repeats):
    func()
end = perf_counter()
elapsed_nested_direct_symbol = end - start
print(f'Elapsed: {elapsed_nested_direct_symbol}')
#Elapsed: 14.60262281403945
compare_timings(elapsed_nested_fully_qualified, elapsed_nested_direct_symbol)
#Timings(timing_1=5.0, timing_2=14.6, abs_diff=9.56, rel_diff_perc=189.64)
#That was significantly slower! Even in absolute terms this is starting to get sloooow.

#So does this mean you should put imports inside functions?

#No, of course not - follow the convention, it makes code far more readable, and of course optimize your code only once you have identified the bottlenecks.

#Does this mean you shouldn't care at all about the performance of your code based on the import variants?

#Again, of course not - you absolutely should.
'''

But, there is absolutely no reason to re-write your code from

import math
math.sqrt(2)

to

from math import sqrt
sqrt(2)

for speed reasons if during the entire lifetime of your application you only call that function 100 times... or 10,000,000 times.

Really depends on your circumstance - be aware of it, but don't try to optimize code until you know where you need to optimize!

[I've seen people refactor parts of their code for sub-second improvements, when, in fact, the largest bottleneck was that they were opening and closing database connections at every read and write instead of pooling connections or something like that]

And

from module import *

has its uses as we'll see later when we discuss packages.

It's not evil, just not very safe - again depends on your circumstance.
