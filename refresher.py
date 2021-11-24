a= [1,2,3]                                                 
#Out: [1, 2, 3]

b=[1,
   2,
   3]                                                      
#Out: [1, 2, 3]

c = [1 #comment1,
     2]                                                    
#Out : 2]
#  ^
# SyntaxError: invalid syntax

#to fix this

c = [1,#comment1                                         
     2]
#Out : [1,2]

#OR

c = [1 #comment1                                         
    ,2]
#Out : [1,2]


#tuples
a = (1,
    2,
    3 #comment)
     #this is an invalid code as the closing parantesis is part of the comment
#out: SyntaxError: unexpected EOF while parsingSyntaxError: unexpected EOF while parsing
#instead try this
     
a = (1,
    2#comment
    )
#out : (1, 2)
    
a = {'Key1':1#comment
    ,'key2':2}
#out :(1, 2)
     
#We can also break up function arguments and parameters:
def my_func(a, #some comment
           b, c):
    print(a, b, c)
     
my_func(10, #comment
       20, #comment
       30)
     
#You can use the \ character to explicitly create multi-line statements.
a = 10
b = 20
c = 30
if a > 5 \
    and b > 10 \
    and c > 20:
    print('yes!!')
#out : yes!!
     
#The identation in continued-lines does not matter:
a = 10
b = 20
c = 30
if a > 5 \
    and b > 10 \
        and c > 20:
    print('yes!!')
#out: yes!!
     
     
     
'''   
Multi-Line Strings
You can create multi-line strings by using triple delimiters (single or double quotes)
'''
     
a = '''this is
a multi-line string'''
print(a)
'''
o/p:
this is
a multi-line string
'''
a
#op: 'this is\na multi-line string'
     
#Note how the newline character we typed in the multi-line string was preserved. Any character you type is preserved. You can also mix in escaped characters line any normal string.
a = """some items:\n
    1. item 1
    2. item 2"""
print(a)
'''
op:
some items:

    1. item 1
    2. item 2
'''
     
#Be careful if you indent your multi-line strings - the extra spaces are preserved!
def my_func():
    a = '''a multi-line string
    that is actually indented in the second line'''
    return a
     
print(my_func())
'''
op:
a multi-line string
    that is actually indented in the second line
'''
#in the above example, there are some extra spaces added.
def my_func():
    a = '''a multi-line string
that is not indented in the second line'''
    return a
print(my_func())
'''
op:
a multi-line string
that is actually indented in the second line
'''
# in this above example, we are not crossing the rules of indentation.
