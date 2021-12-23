'''
Variables are the name given to memory object references

if we say my_var =10
we are pointing towards some memory say 0x1000 and the name for that reference is my_var
now, if we changed the value of my_var =15
now my_var is referenig to some different location say 0X10023

'''

my_var =10
print(hex(id(my_var))) #op: 0x7ffe42132850

my_var =15
print(hex(id(my_var))) #op: 0x7ffe421328f0

my_var += 40
print(hex(id(my_var))) #op: 0x7ffe42132df0
