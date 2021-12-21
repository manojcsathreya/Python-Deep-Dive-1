#built-in functions
s = [1,2,4]
print(len(s))
#op : 3

#we can also import the functiosn from modules-reuseability
import math
print(math.sqrt(4))
print(math.pi)
print(math.exp(1))
'''
OP:
2.0
3.141592653589793
2.718281828459045
'''

#we can also define our function
'''
Syntax

def functionName(parameters):
    body
'''

def func_1():
    print('running func_1')
    
func_1
#op: <function __main__.func_1()> were are not invoking the function here


func_1()
#op : running func_1

#we cannot specify the datatypes for the params of a function
def func_1(a,b):
    print(a*b)
    
func_1(2, 3)
#op: 6

#however we can just specify the data type we are looking for. ANd, this is just for documentation ourspose and this does not have any effect on runnig the program
def func_1(a: int, b : int):
    print(a*b)
    
func_1(2,3)
#op: 6

func_1('a',3)
#op : a,a,a

func_1([1,2,3],2)
#op: [1,2,3,1,2,3]

#the annotation in func paramerer did not stop us from sending other data types as params

# order of defining functions does not matter as long as the functions are not invoked
#ex.
def func_4():
    print(func_3())
    
def func_3():
    return('running func_3')

func_4()

#op: running func_3

#in the above example we have defined the function 3 before the func_4 is invoked. so this worked just fine
#ex 2
def func_7():
    print(func_8())
    
func_7()
def func_8():
    return('running func_5')

#OP: NameError: name 'func_8' is not defined

print(type(func_7))
#<class 'function'>
