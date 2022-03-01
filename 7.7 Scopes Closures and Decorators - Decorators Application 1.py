def timer(fn):
    from time import perf_counter
    from functools import wraps
    
    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args,**kwargs)
        end = perf_counter()
        elapsed = end-start
        
        args_ = [str(a) for a in args]
        kwargs_ = ['{0}={1}'.fomat(k,v) for (k,v) in kwargs.items()]
        all_args = args_+kwargs_
        args_str = ','.join(all_args)
        print('{0}({1}) took {2:.6f}s to run'.format(fn.__name__,
                                                      args_str,
                                                      elapsed))
        return result

    return inner 

'''
we'll write fib numbers in 3 methods
1. Reccursive
2. Loops
3. Reduce function
'''

def calc_reccursive(n):
    if n<=2:
        return 1
    else:
        return calc_reccursive(n-1)+calc_reccursive(n-2)
    
calc_reccursive(1) #1
calc_reccursive(2) #1
calc_reccursive(3) #2
calc_reccursive(4) #3

#if we decorate the calc_reccursive() function it will be timed for all the recursive functions inside it 
# example
@timer
def calc_reccursive(n):
    if n<=2:
        return 1
    else:
        return calc_reccursive(n-1)+calc_reccursive(n-2)
    
calc_reccursive(5)
'''
calc_reccursive(2) took 0.000001s to run
calc_reccursive(1) took 0.000001s to run
calc_reccursive(3) took 0.000860s to run
calc_reccursive(2) took 0.000001s to run
calc_reccursive(4) took 0.003121s to run
calc_reccursive(2) took 0.000001s to run
calc_reccursive(1) took 0.000001s to run
calc_reccursive(3) took 0.000070s to run
calc_reccursive(5) took 0.003274s to run
'''

#so we do the following

@timer
def fib_recurrsed(n):
    return calc_reccursive(n)

fib_recurrsed(5) #fib_recurrsed(5) took 0.000005s to run
fib_recurrsed(10) #fib_recurrsed(10) took 0.000108s to run
fib_recurrsed(18) #fib_recurrsed(18) took 0.002856s to run
fib_recurrsed(30) #fib_recurrsed(30) took 1.074777s to run

#as you see the run time is increasing substantially
fib_recurrsed(35) #fib_recurrsed(35) took 14.611121s to run 9227465

#We'll try with loop now
@timer
def fib_loop(n):
    fib1, fib2 = 1,1
    for i in range(3,n+1):
        fib1,fib2 = fib2, fib1+fib2
    return fib2

fib_loop(6) #fib_loop(6) took 0.000014s to run 8

fib_loop(30) #fib_loop(30) took 0.000006s to run  832040
#runs a way lot faster

#using reduce funtion
from functools import reduce
@timer
def fib_reduce(n):
    initial = (1,0)
    dummy = range(n)
    res = reduce(lambda prev,n:(prev[0]+prev[1], prev[0]),dummy,initial)
    return res[0]

fib_reduce(30) #fib_reduce(30) took 0.000016s to run
fib_loop(30) #fib_loop(30) took 0.000006s to run

fib_reduce(100) #fib_reduce(100) took 0.000047s to run
fib_loop(100) #fib_loop(100) took 0.000020s to run
#you can see loop runs much faster than reduce method

#maybe we want to run the timer for n number of times ad the take the avg

def timer(fn):
    from time import perf_counter
    from functools import wraps
    
    @wraps(fn)
    def inner(*args, **kwargs):
        elapsed_total = 0
        elapsed_count= 0
        for i in range(10):
            print('Iteration {0} runing...'.format(i))
            start = perf_counter()
            result = fn(*args,**kwargs)
            end = perf_counter()
            elapsed = end-start
            elapsed_total += elapsed
            elapsed_count+=1
        
        args_ = [str(a) for a in args]
        kwargs_ = ['{0}={1}'.fomat(k,v) for (k,v) in kwargs.items()]
        all_args = args_+kwargs_
        args_str = ','.join(all_args)
        elapsed_avg = elapsed_total/elapsed_count
        print('{0}({1}) took {2:.6f}s to run'.format(fn.__name__,
                                                      args_str,
                                                      elapsed_avg))
        return result

    return inner 

@timer
def fib_reduce(n):
    initial = (1,0)
    dummy = range(n)
    res = reduce(lambda prev,n:(prev[0]+prev[1], prev[0]),dummy,initial)
    return res[0]

fib_reduce(100)
'''
Iteration 0 runing...
Iteration 1 runing...
Iteration 2 runing...
Iteration 3 runing...
Iteration 4 runing...
Iteration 5 runing...
Iteration 6 runing...
Iteration 7 runing...
Iteration 8 runing...
Iteration 9 runing...
fib_reduce(100) took 0.000089s to run
'''
#what can we do to specify the number that we need to run?
def timer(fn,count):
    from time import perf_counter
    from functools import wraps
    
    @wraps(fn)
    def inner(*args, **kwargs):
        elapsed_total = 0
        elapsed_count= 0
        for i in range(count):
            print('Iteration {0} runing...'.format(i))
            start = perf_counter()
            result = fn(*args,**kwargs)
            end = perf_counter()
            elapsed = end-start
            elapsed_total += elapsed
            elapsed_count+=1
        
        args_ = [str(a) for a in args]
        kwargs_ = ['{0}={1}'.fomat(k,v) for (k,v) in kwargs.items()]
        all_args = args_+kwargs_
        args_str = ','.join(all_args)
        elapsed_avg = elapsed_total/elapsed_count
        print('{0}({1}) took {2:.6f}s to run'.format(fn.__name__,
                                                      args_str,
                                                      elapsed_avg))
        return result

    return inner 

def fib_reduce(n):
    initial = (1,0)
    dummy = range(n)
    res = reduce(lambda prev,n:(prev[0]+prev[1], prev[0]),dummy,initial)
    return res[0]


fib_reduce = timer(fib_reduce,15)
fib_reduce(100)
'''
Iteration 0 runing...
Iteration 1 runing...
Iteration 2 runing...
Iteration 3 runing...
Iteration 4 runing...
Iteration 5 runing...
Iteration 6 runing...
Iteration 7 runing...
Iteration 8 runing...
Iteration 9 runing...
Iteration 10 runing...
Iteration 11 runing...
Iteration 12 runing...
Iteration 13 runing...
Iteration 14 runing...
fib_reduce(100) took 0.000066s to run
'''
#or we can use parameterized decorator
#ex: timer(15)

