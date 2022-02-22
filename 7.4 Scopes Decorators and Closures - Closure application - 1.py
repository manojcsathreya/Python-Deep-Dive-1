#Closures application

class averager:
    def __init__(self):
        self.numbers = []
        
    def add(self, number):
        self.numbers.append(number)
        self. total = sum(self.numbers)
        self.count = len(self.numbers)
        return self.total/self.count
    
a =  averager()
a.add(10) #10.0
a.add(20) #15.0
a.add(30) #20.0


#with closures
def averager():
    numbers = []
    
    def add(number):
        numbers.append(number)
        total = sum(numbers)
        count = len(numbers)
        return total/count
    return add

a = averager()   
a(10) #10.0
a(20)#15.0
a(30)#20.0

'''
Now, instead of storing a list and reclaculating total and count every time wer need the new average, we are going to store the running total and count and update each value each time a new value is added to the running average, and then return total / count.

Let's start with a class approach first, where we will use instance variables to store the running total and count and provide an instance method to add a new number and return the current average.
'''

class Averager():
    def __init__(self):
        self.count = 0
        self.total = 0
        
    def add(self,number):
        self.total+= number
        self.count+=1
        return self.total/self.count
    
a = Averager()
a.add(10) #10.0
a.add(20) #15.0
a.add(30) #20.0


def Averager():
    count, total = 0,0
    
    def add(val):
        nonlocal total,count
        total += val
        count+=1
        return 0 if count == 0 else total/count
    
a = averager()   
a(10) #10.0
a(20)#15.0
a(30)#20.0

'''
Generalizing this example
We saw that we were essentially able to convert a class to an equivalent functionality using closures. This is actually true in a much more general sense - very often, classes that define a single method (other than initializers) can be implemented using a closure instead.

Let's look at another example of this.

Suppose we want something that can keep track of the running elapsed time in seconds.
'''
from time import perf_counter

class Timer:
    def __init__(self):
        self.start = perf_counter()
    def __call__(self):
        return (perf_counter() - self.start)
        
a = Timer()
a()

b = Timer()
print(a())
print(b())

#rewritting in closure

def Timer():
    start = perf_counter()
    
    def elapsed():
        # we don't even need to make start nonlocal 
        # since we are only reading it
        return (perf_counter() - start)
    return elapsed

x = Timer()
x() #5.4303910000016

        
