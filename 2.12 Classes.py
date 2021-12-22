#classes

# we can use anything in place of self. but it is good to use self for user readability
class Rectangle:
    def __init__(self,height,width):
        self.height= height
        self.width=width
        
    def area(self):
        return self.height*self.width
    
    def perimeter(self):
        return 2*(self.width+self.height)
    
r1 = Rectangle(10, 20)
print(r1.area())
print(r1.perimeter()) #op: 200,60

#we have special functions to verride the predefined meaning
#overiding str method
class Rectangle:
    def __init__(self,height,width):
        self.height= height
        self.width=width
        
    def area(self):
        return self.height*self.width
    
    def perimeter(self):
        return 2*(self.width+self.height)
    
    def __str__(self):
        return ('{0} is the height and {1} is the width'.format(self.height,self.width))
    
r1 = Rectangle(10, 20)

print(r1.area())
print(r1.perimeter())

str(r1)
#op:'10 is the height and 20 is the width'



