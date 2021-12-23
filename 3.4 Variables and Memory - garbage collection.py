'''

'''


import ctypes
import gc
import sys

def ref_count(address):
    return ctypes.c_long.from_address(address).value

def object_by_id(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return 'Object exists'
        else:
            return 'not found'
        
class A:
    def __init__(self):
        self.b = B(self)
        print('self:A:{0}, b:{1}'.format(hex(id(self)),hex(id(self.b))))

class B:
    def __init__(self,a):
        self.a = a
        print('self:B:{0}, b:{1}'.format(hex(id(self)), hex(id(self.a))))

gc.disable()

my_var = A()      

'''
self:B:0x1f649eef070, b:0x1f649eef220
self:A:0x1f649eef220, b:0x1f649eef070
'''  

print(hex(id(my_var)))
print(hex(id(my_var.b)))
print(hex(id(my_var.b.a)))            

'''
0x1f649eef220
0x1f649eef070
0x1f649eef220
'''
a_id = id(my_var)
b_id = id(my_var.b)

print(hex(a_id))
print(hex(b_id))

'''
0x1f649eef220
0x1f649eef070
'''

print(ref_count(a_id))#2
print(ref_count(b_id))#1

print(object_by_id(a_id))#Object exists
print(object_by_id(b_id))#Object exists

my_var = None

print(ref_count(a_id))#1
print(ref_count(b_id))#1

#this is an example of circular reference
#running GC manually
gc.collect()

print(object_by_id(a_id)) # not found
print(object_by_id(b_id)) # not found


print(ref_count(a_id))#some junk and always changes
print(ref_count(b_id))# some junk and always changes


#but object_by_id() returns not found. This is why we should not play with memory in python unless we need it badly

