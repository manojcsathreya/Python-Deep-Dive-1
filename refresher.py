a= [1,2,3]                                                 #Out: [1, 2, 3]

b=[1,
   2,
   3]                                                      #Out: [1, 2, 3]

c = [1 #comment1,
     2]                                                    #Out : 2]
                                                                #  ^
                                                                # SyntaxError: invalid syntax
#to fix this      
c = [1,#comment1                                           #Out : [1,2]
     2]
#OR

c = [1 #comment1                                           #Out : [1,2]
    ,2]

