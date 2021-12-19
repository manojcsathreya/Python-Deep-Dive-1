#identifiers are case sensitive
#must start with underscore or letters followed by underscore or letter or numbers
#cannot be identifiers
'''
when an identifiers starts with single underscore: This is a convention followed to indicate that the identifier as an private variable
when an identifiers starts with double underscore : This is a convention followed to indicate that the identifier is used in inheritance
when an identifiers starts with double underscore and ends with double underscore: used for system defined, and has special meaning to interpreter(Don;t invent one. Just use the pre defined ones)
'''
'''
Naming conventions prescribed in pep8
Packages : short, all-lowercase names. Preferably no underscores. : example: utilities
Modules: short, all-lowercase names. Can have underscores.
Packages : short, all-lowercase names. Preferably no underscores. : Example-utilities
db_utils dbutils
Classes : CapWords (upper camel case) :Example- BankAccount
Functions : lowercase, words separated by underscores (snake_case) :Example-open_account
Variables : lowercase, words separated by underscores (snake_case) : Example-account_id
Constants : all-uppercase, words separated by underscores : Example-MIN_APR
'''

#3. Conditional statements

a=5
if a <5:
    print('a<5')
else:
    if a<10:
        print('5<=a<10')
    else:
        print('a>=10')
   #op: 5<=a<10      

a=10
if a <5:
    print('a<5')
else:
    if a<10:
        print('5<=a<10')
    else:
        print('a>=10')
        
        #op: a>=10

a=6
if a <5:
    print('a<5')
else:
    if a<10:
        print('5<=a<10')
    else:
        print('a>=10')
        
        #op: 5<=a<10
        
        
# we do not have switch statements in python
#instaed we use elif

a = 4

if a<5:
    print('a<5')
elif a<10:
    print('5<=a<10')
elif a<15:
    print('10<=a<15')
elif a<20:
    print('15<=a<20')
else:
    print(a>=20)
#op:a<5

a = 6

if a<5:
    print('a<5')
elif a<10:
    print('5<=a<10')
elif a<15:
    print('10<=a<15')
elif a<20:
    print('15<=a<20')
else:
    print(a>=20)
#op:<=a<10

a = 10

if a<5:
    print('a<5')
elif a<10:
    print('5<=a<10')
elif a<15:
    print('10<=a<15')
elif a<20:
    print('15<=a<20')
else:
    print(a>=20)
#op:10<=a<15

a = 20

if a<5:
    print('a<5')
elif a<10:
    print('5<=a<10')
elif a<15:
    print('10<=a<15')
elif a<20:
    print('15<=a<20')
else:
    print('a>=20')
#op:a>=20

#we also have ternary operator
#syntax return a if true else return b
a=4
print('a<5' if a<5 else 'a>5')
