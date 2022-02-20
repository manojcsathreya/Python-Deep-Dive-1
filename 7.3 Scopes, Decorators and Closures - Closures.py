'''
Closures

Free Variables and Closures
Remember: Functions defined inside another function can access the outer (nonlocal) variables
def outer():
    x = 'python'                               this x refers to the one in outer's scope
    def inner():
        print("{0} rocks!".format(x))
    inner()

outer() →python rocks!

this nonlocal variable x is called a free variable
when we consider inner, we really are looking at:
• the function inner
• the free variable x(with current value python)

This is called a closure
---------------------------------------------------------------------------------------
Returning the inner function
What happens if, instead of calling (running) innerfrom inside outer, we return it? 
def outer():
    x = 'python'
    def inner():
        print("{0} rocks!".format(x))
    return inner

x is a free variable in inner it is bound to the variable x in outer this happens when outer runs (i.e. when inner is created)

We can assign that return value to a variable name: fn = outer()

when we return inner, we are actually "returning" the closure

fn() →python rocks!

When we called fn
at that time Python determined the value of x in the extended scope
But notice that outer had finished running before we called fn– it's scope was "gone"
---------------------------------------------------------------------------------------
Python Cells and Multi-Scoped Variables
def outer():
    x = 'python'
    def inner():
        print(x)
    return inner

Here the value of xis shared between two scopes:
• outer
• closure
The label x is in two different scopes but always reference the same "value"
Python does this by creating a cell as an intermediary object

outer.x    ---> cell <0xA500>  ---->   str <0xFF100> --->  indirect reference
inner.x              0xFF100                python

In effect, both variables x(in outerand inner), point to the same cell
When requesting the value of the variable, Python will "double-hop" to get to the final value
---------------------------------------------------------------------------------------
Closures

You can think of the closure as a function plus an extended scope that contains the free variables

The free variable's value is the object the cell points to – so that could change over time!
Every time the function in the closure is called and the free variable is referenced:
Python looks up the cell object, and then whatever the cell is pointing to

def outer():
    a = 100
    x = 'python'
    def inner():
        a = 10  # local variable
        print("{0} rocks!".format(x))  --> x is a closure  -->  cell  <0xA500>  -->  str  <0xFF100>
    return inner                                                      0xFF100              python
fn = outer()

fn → inner + extended scope x
---------------------------------------------------------------------------------------
Introspection
def outer():
    a = 100
    x = 'python'
    def inner():
        a = 10  # local variable
        print("{0} rocks!".format(x))  --> x is a closure  -->  cell  <0xA500>  -->  str  <0xFF100>
    return inner                                                      0xFF100              python
fn = outer()
fn.__code__.co_freevars →('x',) (a is not a free variable)
fn.__closure__ → (<cell at 0xA500: str object at 0xFF100>, )



def outer():
    x = 'python'
    print(hex(id(x))    --> 0xFF100
    def inner():
        print(hex(id(x))  --> 0xFF100
        print("{0} rocks!".format(x))
    return inner
fn = outer()
fn()
---------------------------------------------------------------------------------------

Modifying free variables

def counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc

closure count is a free variable it is bound to the cell count

fn = counter()  →inc+ count → 0

fn() → 1  count's (indirect) reference changed from the object 0 to the object 1

fn() → 2
---------------------------------------------------------------------------------------
Multiple Instances of Closures
Every time we run a function, a new scope is created.
If that function generates a closure, a new closure is created every time as well

def counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc

f1 = counter()
f2 = counter()
f1() → 1
f1() → 2
f1() → 3

f2() → 1

f1 and f2 do not have the same extended scope they are different instances of the closure

the cells are different

---------------------------------------------------------------------------------------
Shared Extended Scopes

def outer():
    count = 0
    def inc1():
        nonlocal count   --> count is a free variable – bound to countin the extended scope
        count += 1
        return count
    def inc2():
        nonlocal count   --> countis a free variable – bound to the same count
        count += 1
        return count
    return inc1, inc2    --> returns a tuple containing both closures

f1, f2 = outer()
f1() → 1
f2() → 2

You may think below shared extended scope is highly unusual… but it's not!
def adder(n):
    def inner(x):
        return x + n
    return inner

add_1 = adder(1)
add_2 = adder(2)
add_3 = adder(3)

Three different closures – no shared scopes

add_1(10)  → 11
add_2(10)  → 12
add_3(10)  → 13


But suppose we tried doing it this way:
adders = []
for n in range(1, 4):
    adders.append(lambda x: x + n)

Now we could call the adders in the following way:

n = 1: the free variable in the lambda is n, and it is bound to the nwe created in the loop
n = 2: the free variable in the lambda is n, and it is bound to the (same) nwe created in the loop
n = 3: the free variable in the lambda is n, and it is bound to the (same) nwe created in the loop

adders[0](10)  →13
adders[1](10)  →13
adders[2](10)  →13

Remember, Python does not "evaluate" the free variable nuntil the adders[i] function is called
Since all three functions in adders are bound to the same n by the time we call adders[0], the value of n is 3
(the last iteration of the loop set n to 3)
---------------------------------------------------------------------------------------

Nested Closures
def incrementer(n):
    # inner + n is a closure
    def inner(start):
        current = start
        # inc + current + n is a closure
        def inc():
            nonlocal current
            current += n
            return current
        return inc
    return inner

(inner)
fn = incrementer(2) →fn.__code__.co_freevars → 'n'  n=2
(inc)
inc_2 = fn(100) →inc_2.__code__.co_freevars → 'current', 'n'
                                                current=100, n=2

(calls inc)
inc_2() →102  (current = 102, n=2)
inc_2() →104  (current = 104, n=2)
---------------------------------------------------------------------------------------

'''

#Closures
def outer():
    x = 'python'
    def inner():
        print(x)
    return inner
    
fn = outer() 

fn.__code__.co_freevars #('x',)

fn.__closure__ #(<cell at 0x0000022B52B34190: str object at 0x0000022B4BE43470>,)

def outer():
    x = [1,2,3]
    print('Outer x ',hex(id(x)))
    def inner():
        print('Inner x',hex(id(x)))
        print(x)
    return inner

fn = outer() #Outer x  0x22b527d0d80
fn() #Inner x 0x22b527d0d80 [1, 2, 3]
fn.__closure__ #(<cell at 0x0000022B52B34DF0: list object at 0x0000022B527D0D80>,)

#modifying a free variable

def counter():
    count = 0
    def inc():
        nonlocal count
        count+=1
        print(count)
    return inc

cnt = counter()
cnt() #1
cnt() #2

cnt2 = counter()
cnt2() #1

#cnt and cnt2 does not share the same scope

#Shared extended scopes

def outer():
    count = 0
    def inc1():
        nonlocal count
        count +=1
        print(count)
    def inc2():
        nonlocal count
        count +=1
        print(count)
    return inc1,inc2

fn1,fn2 = outer()
fn1()#1
fn2() #2
fn2() #3
fn1.__code__.co_freevars#('count',)
fn2.__code__.co_freevars#('count',)

fn1.__closure__ #(<cell at 0x0000022B52B341F0: int object at 0x00007FF973E92770>,)
fn2.__closure__ #(<cell at 0x0000022B52B341F0: int object at 0x00007FF973E92770>,)


#everytime timea function is called a new local scope is created
#EX
from time import perf_counter

def func():
    x = perf_counter()
    print(x,hex(id(x)))
    
func() #185119.7753288 0x22b52b481d0
func() #185133.6054464 0x22b52b487d0

def pow(x):
    def inner(n):
        return n**x
    return inner
square = pow(2)
square(5) #25
cube = pow(3)
cube(5) #125

square.__closure__ #(<cell at 0x0000022B52B34D90: int object at 0x00007FF973E92750>,)
cube.__closure__ #(<cell at 0x0000022B52B349D0: int object at 0x00007FF973E92770>,)
print(hex(id(2)))#0x7ff973e92750
print(hex(id(3))) #0x7ff973e92770

#BEWARE
def adder(n):
    def inner(x):
        return x+n
    return inner

add_1 = adder(1)
add_2 = adder(2)
add_3 = adder(3)
add_4 = adder(4)
add_1(10)#11
add_2(12)#14
add_3(10)#13
add_4(14)#18

#we get a little fancy

def createadders():
    adders = []
    for i in range(1,4):
        adders.append(lambda x: x+i)
    return adders

adders = createadders()
print(adders[0],adders[1],adders[2])
'''
<function createadders.<locals>.<lambda> at 0x0000022B52B2A9D0> 
<function createadders.<locals>.<lambda> at 0x0000022B52749790> 
<function createadders.<locals>.<lambda> at 0x0000022B52B54040>'''

adders[0](10) #13
adders[1](10) #13
adders[2](10) #13       
#woah
#what happended here?

adders[0].__code__.co_freevars #('i',)

adders[0].__closure__ #(<cell at 0x0000022B52B498E0: int object at 0x00007FF973E92770>,)
adders[1].__closure__ #(<cell at 0x0000022B52B498E0: int object at 0x00007FF973E92770>,)
adders[2].__closure__ #(<cell at 0x0000022B52B498E0: int object at 0x00007FF973E92770>,)

#what every int is referring to same object
hex(id(3))     #'0x7ff973e92770'
#every object is referring to 3
#what happened here is during function creation python does not initiate any varibles inside the function
#python just creates the function and when called it executes. till then it just knows that it need to refer n but when value of n changes after all the iteration
#it does not care
#simple hack to solve this is making the n a default param
#remember, only definition and params are evaluated at compile time

def create_adders():
    adders = []
    for i in range (4):
        adders.append(lambda x,step = i: x+step)
    return adders
adders =  create_adders()
adders[0].__closure__
adders[1].__closure__
adders[2].__closure__
#empty
#why
#what about free vars
adders[0].__code__.co_freevars  #()
'''
Hmm, nothing either... Why?

Well, look at the lambda in that loop. Does it reference the variable n (other than in the default value)? No. Hence, n is not a free variable in this case, and our lambda is just a plain lambda, not a closure.
'''       
print(adders[0](10),adders[1](10),adders[2](10),adders[3](10)) #10 11 12 13

'''
You just need to understand that since the default values are evaluated when the function (lambda in this case) is created, the then-current n value is assigned to the local variable step. So step will not change every time the lambda is called, and since n is not referenced inside the function (and therefore evaluated when the lambda is called), n is not a free variable.
'''

print(adders[0](10,10)) #20

#nested Closure
def incrementer(n):
    def inner(start):
        current = start
        def inc():
            a = 10
            nonlocal current
            current +=n
            return current
        return inc
    return inner

fn = incrementer(2)
fn #<function __main__.incrementer.<locals>.inner(start)>
fn.__code__.co_freevars #('n',)
fn.__closure__#(<cell at 0x0000022B52B49670: int object at 0x00007FF973E92750>,)
inc_2 = fn(100)
inc_2 #<function __main__.incrementer.<locals>.inner.<locals>.inc()>
inc_2.__code__.co_freevars #('current', 'n')
inc_2.__closure__
'''
(<cell at 0x0000022B52A999D0: int object at 0x00007FF973E93390>,
 <cell at 0x0000022B52B49670: int object at 0x00007FF973E92750>)
'''
inc_2() #102
inc_2()#104
inc_3 = incrementer(3)(200)
inc_3()#203
inc_3()#206
