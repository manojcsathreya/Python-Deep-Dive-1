'''
Scopes and Namespaces

a = 10

That object can be accessed using that name in various parts of our code
But not just anywhere!

That variable name and it's binding (name and object) only "exist" in specific parts of our code
the portion of code where that name/binding is defined, is called the lexical scope of the variable
these bindings are stored in namespaces

When an object is assigned to a variable
that variable points to some object

and we say that the variable (name) is bound to that object

(each scope has its own namespace)

The Global Scope

The global scope is essentially the module scope.

It spans a single file only.

There is no concept of a truly global (across all the modules in our entire app) scope in Python

The only exception to this are some of the built-in globally available objects, 
such as:True False None dict print

The built-in and global variables can be used anywhere inside our module
including inside any function
--------------------------------------------------------------------------------
Global scopes are nested inside the built-in scope

If you reference a variable name inside a scope and Python does not find it in that scope's namespace
it will look for it in an enclosing scope's namespace

Built-in Scope             name space
name space                 var1 0xA345E
                           func1 0xFF34A

Module Scope
name space

Module2 Scope
name space
-----------------------------------------------------------------------------------
Examples

module1.py
print(True) → True

Python does not find Trueor printin the current (module/global) scope
So, it looks for them in the enclosing scope →built-in. Finds them there

module2.py
print(a)   → run-time Name Error

Python does not find aor printin the current (module/global) scope
So, it looks for them in the enclosing scope →built-in
Find print, but not a


module3.py
print = lambda x: 'hello {0}!'.format(x)
s = print('world') 

Python finds print in the module scope <Beware that the local print function overrides the actual print function>
So it uses it!
s → hello world!

to delete it we use del print
-----------------------------------------------------------------------------------
The Local Scope

When we create functions, we can create variable names inside those functions (using assignments

     e.g. a = 10                                                                          e.g. a = 10
        
Variables defined inside a function are not created until the function is called

Every time the function is called, a new scope is created (this is why recursion works!)
                                                                       
Variables defined inside the function are assigned to that scope →Function Local scope
                                                                 →Local scope

The actual object the variable references could be different each time the function is called

Every time the function is called, a new scope is created
-----------------------------------------------------------------------------------
Example

def my_func(a, b):
    c = a * b
    return c

my_func  
a
b
c

these names will considered local to my_func

my_func('z', 2)

my_func
a→'z'
b→2
c→'zz'

has different local space

my_func(10, 5)

my_func
a→10
b→5
c→50

same names, different local scopes
-----------------------------------------------------------------------------------
Nested Scopes

Scopes are often nested

Built-in Scope

Module Scope

Local Scope   Local Scope     Local Scope

Namespace lookups

When requesting the object bound to a variable name:
    
    e.g. print(a)

Python will try to find the object bound to the variable
• in current local scope first
• works up the chain of enclosing scopes


Example
module1.py

a = 10

def my_func(b):
    print(True)
    print(a)
    print(b)


built-in scope     True

global scope       a→10  my_func

When we call 
my_func('a')

local scope        b→'a'

my_func(300)

local scope        b→300 

Remember reference counting?
When my_func(var) finishes running, the scope is gone too!
and the reference count of the object varwas bound to (referenced) is decremented 
We also say that vargoes out of scope
------------------------------------------------------------------------------

Accessing the global scope from a local scope

When retrieving the value of a global variable from inside a function, Python automatically
searches the local scope's namespace, and up the chain of all enclosing scope namespaces
local →global →built-in

What about modifying a global variables value from inside the function?

a = 0
def my_func():
    a = 100             assignment →Python interprets this as a local variable (at compile-time)    
    print(a)                  →the local variable amasks the global variable a
    
my_func()  → 100
print(a) → 0 


built-in

global   a→0  my_func

local   a→100

-------------------------------------------------------------------------------
The globalkeyword
We can tell Python that a variable is meant to be scoped in the global scope 
by using the globalkeyword

a = 0
def my_func():
    global a
    a = 100
    
my_func()
print(a)  → 100

built-in

global      a→0        my_func

local

Example

counter = 0

def increment():
    global counter
    counter += 1
    
increment()
increment()
increment()
print(counter) → 3
----------------------------------------------------------------------------------
Global and Local Scoping
When Python encounters a function definition at compile-time
it will scan for any labels (variables) that have values assigned to them (anywhere in the function)
if the label has not been specified as global, then it will be local
variables that are referenced but not assigned a value anywhere in the function will not be local, 
and Python will, at run-time, look for them in enclosing scopes

a = 10

def func1():
    print(a)   a is referenced only in entire function at compile time →a non-local

def func2():
    a = 100    assignment at compile time →a local
    
def func3():
    global a
    a = 100    assignment at compile time →a global(because we told Python a was global)

def func4():
    print(a)   assignment at compile time →a local
    a = 100

→when we call func4()
print(a) results in a run-time error
    because a is local, and we are referencing it before we have assigned a value to it!

'''
#In Python the global scope refers to the module scope.

#The scope of a variable is normally defined by where it is (lexically) defined in the code.

a = 10

#In this case, a is defined inside the main module, so it is a global variable.

def my_func(n):
    c = n ** 2
    return c

#In this case, c was defined inside the function my_func, so it is local to the function my_func. In this example, n is also local to my_func

def my_func(n):
    print('global:', a)
    c = a ** n 
    return c

my_func(2) #global: 100

def my_func(n):
    a = 2
    c = a ** 2
    return c

print(a) #10
print(my_func(3)) #4
print(a) #10

#break

a = 10

def my_func(n):
    global a
    a = 2
    c = a ** 2
    return c

print(a) #10
print(my_func(3)) #4
print(a) #2 

#break

def my_func(n):
    global var
    var = 'hello world'
    return n ** 2

#Now, var does not exist yet, since the function has not run:
print(var)
'''---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-10-571cba235a7f> in <module>()
----> 1 print(var)

NameError: name 'var' is not defined'''

my_func(2) #calling the function mean python creates a function and thier name scpaces
#now if we print var
print(var) # 'hello world'


#Beware!!
#Remember that whenever you assign a value to a variable without having specified the variable as global, it is local in the current scope. Moreover, it does not matter where the assignment in the code takes place, the variable is considered local in the entire scope - Python determines the scope of objects at compile-time, not at run-time.
#Let's see an example of this:
    
a = 10
b = 100

def my_func():
    print(a)
    print(b)

my_func() #10 100

#So, this works as expected - a and b are taken from the global scope since they are referenced before being assigned a value in the local scope.

#But now consider the following example:
    
    
#break

a = 10
b = 100

def my_func():
    print(a)
    print(b)
    b = 1000
    '
my_func()

'''
10
---------------------------------------------------------------------------
UnboundLocalError                         Traceback (most recent call last)
<ipython-input-17-d82eda95de40> in <module>()
----> 1 my_func()

<ipython-input-16-a2b60f95cac1> in my_func()
      4 def my_func():
      5     print(a)
----> 6     print(b)
      7     b = 1000

UnboundLocalError: local variable 'b' referenced before assignment
'''
#As you can see, b in the line print(b) is considered a local variable - that's because the next line assigns a value to b - hence b is scoped as local by Python for the entire function.
#Of course, functions are also objects, and scoping applies equally to function objects too. For example, we can "mask" the built-in print Python function:
    
print = lambda x: 'hello {0}!'.format(x)

def my_func(name):
	return print(name)

my_func('world') #print = lambda x: 'hello {0}!'.format(x)

def my_func(name):
	return print(name)

my_func('world')  #'hello world!'

#to get print function  back

del print
print('hello') #'hello'


'''If you have experience in some other programming languages you may be wondering if loops and other code "blocks" have their own local scope too. For example in Java, the following would not work:

for (int i=0; i<10; i++) {
    int x = 2 * i;
}
system.out.println(x);

But in Python it works perfectly fine:'''
for i in range(10):
    x = 2 * i
print(x) #18

#In this case, when we assigned a value to x, Python put it in the global (module) scope, so we can reference it after the for loop has finished running.
