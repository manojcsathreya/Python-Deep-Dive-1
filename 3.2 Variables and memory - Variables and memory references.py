#variable names are aliases for memory adderess
#Storing and retriving from heap memory is done by python memory manager

my_var = 10
print(id(my_var)) #140730006972496
print(hex(id(my_var))) #0x7ffe42132850
#id function is used to fetch the memory location of the variable and to convert that to hex we use hex
