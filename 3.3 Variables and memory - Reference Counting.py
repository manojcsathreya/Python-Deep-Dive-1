import sys
#reference counting
my_var = 10
#my_var is referencing one memory say,0x1000. in this case the reference to the object containing 10 in memory is one
other_var = my_var
#other var is also referencing to the same object in the memory
#reference count is 2 .
#how to ge t the reference count?
sys.getrefcount(my_var) #20

import sys
import ctypes
a = [1,2,3]
print(id(a))#2157313519040
print(sys.getrefcount(a))#2
b = a
print(sys.getrefcount(a))#3

def get_ref(id:int):
    return ctypes.c_long.from_address(id).value

#ctypes does not include another pointer to get reference. getrefcount will.

print(get_ref(id(a))) #2

c=a
print(get_ref(id(a))) #3

c= None
print(get_ref(id(a))) #2

b =10
print(get_ref(id(a))) #1

id_a = id(a)
print(get_ref(id_a))#1
a=10
print(get_ref(id_a))# some junk value because the cleaned up memory will be used for other objects
