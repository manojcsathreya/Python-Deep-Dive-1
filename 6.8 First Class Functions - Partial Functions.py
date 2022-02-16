'''
Reducing Function Arguments

def my_func(a, b, c):
    print(a, b, c)

def fn(b, c):
    return my_func(10, b, c)

f = lambda b, c: my_func(10, b, c)

fn(20, 30)  → 10, 20, 30

f(20, 30)   → 10, 20, 30


from functools import partial
f = partial(my_func, 10)
f(20, 30) → 10, 20, 30


Handling more complex arguments

def my_func(a, b, *args, k1, k2, **kwargs):
    print(a, b, args, k1, k2, kwargs)

def f(b, *args, k2, **kwargs):
    return my_func(10, b, *args, k1='a', k2=k2, **kwargs)
OR
f = partial(my_func, 10, k1='a')

Handling more complex arguments

def pow(base, exponent):
    return base ** exponent

square = partial(pow, exponent=2)
cube = partial(pow, exponent=3)

square(5)  → 25

cube(5)   → 125

cube(base=5) → 125

BEWARE!! 
square(5, exponent=3) → 125 wecan override the pramas

Beware!!
You can use variables when creating partials

def my_func(a, b, c):
    print(a, b, c)

a = 10
f = partial(my_func, a)

f(20, 30) → 10, 20, 30

a = 100
f(20, 30) → 10, 20, 30

the memory address of 10is baked in to the partial

a now points to a different memory address
but the partial still points to the original object (10)

If ais mutable (e.g. a list), then it's contents can be changed

but there arises a similar issue to argument default values

'''

def myfunc(a,b,c):
    print(a,b,c)
    
def f1(x,y):
    myfunc(10, x,y)
    
f1(20,30) #10 20 30

f1(100,200) #10 100 200

f = lambda x,y:myfunc(1, x, y)
f(2,3) #1 2 3

from functools import partial

f = partial(myfunc,10)
f(20,30) #10 20 30

f = partial(myfunc,10,20)
f(30) #10 20 30
f(30,40) #TypeError: myfunc() takes 3 positional arguments but 4 were given

f = partial(myfunc,b=20)
f(10,c=30) # 10 20 30

def myfunc(a,b,*args,k1,k2,**kwargs):
    print(a,b,args,k1,k2,kwargs)

myfunc(10,20,30,40,k1='a',k2='b',k3=2000,k4=3000) #10 20 (30, 40) a b {'k3': 2000, 'k4': 3000}

def f1(x,*vars,kw,**kwvars):
    myfunc(10, x, *vars, k1='a', k2=kw, **kwvars)

f1(20,30,40,kw='b',k3='c',k4='d') #10 20 (30, 40) a b {'k3': 'c', 'k4': 'd'}

f = partial(myfunc,10,k1='a')
f(20,30,40,k2='b',k3 = 'c',k4='d') #10 20 (30, 40) a b {'k3': 'c', 'k4': 'd'}

def pow(base,exponent):
    print(base**exponent)

square = partial(pow,exponent=2)
cube= partial(pow,exponent = 3)
square(5) #25
cube(5) #125

#beware

def pow(base,exponent):
    print(base**exponent)

a= 2
sq = partial(pow,exponent=a)   
sq(5) #25
a =3
print(a) #3
sq(5) #25
#because the sq function had the value for exponenet as  2 while function definition. It is trying to retain the same value
#another Example

def f2(a,b):
    print(a,b)
    
x= [2,3,4]
f3 = partial(f2, x)
f3(1) #[2, 3, 4] 1
x.append(5)
f3(1) #[2, 3, 4, 5] 1
#coz the param is mutable
