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
     
     
