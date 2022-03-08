'''
Tuple as Data Structure
We have seen how we interpreted tuples as data structures
The position of the object contained in the tuple gave it meaning
For example, we can represent a 2D coordinate as: (10, 20)
                                                    x   y
If pt is a position tuple, we can retrieve the x and y coordinates using:

x, y = pt 
OR
x = pt[0]
y = pt[1]
So, for example, to calculate the distance of ptfrom the origin we could write:

dist = math.sqrt(pt[0] ** 2 + pt[1] ** 2)

Now this is not very readable, and if someone sees this code they will have to know that pt[0]
means the x-coordinate and pt[1]means the y-coordinate.
This is not very transparent.
------------------------------------------------------------------------------------------
Using a Class Instead
At this point, in order to make things clearer for the reader (not the compiler, the reader), we 
might want to approach this using a class instead.

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Stock:
    def __init__(self, symbol, year, month, day, open, high, low, close):
        self.symbol = symbol
        self.year = year
        self.month = month
        self.day = day
        self.open = open
        self.high = high
        self.low = low
        self.close = close

pt = Point2D(10, 20)
distance = sqrt(pt.x ** 2 + pt.y ** 2)



Class Approach             Tuple Approach
djia.symbol                  djia[0]
djia.open                    djia[4]
djia.close                   djia[7]
djia.high – djia.low         djia[5] – djia[6]
You can see if we use the tuples thing we have to access it by indexing and every time we have to 
look up for the what is the meaning of 0 is or 4 is or 7 is. This is not easy
------------------------------------------------------------------------------------------
Instead if we do class implementation
Extra Stuff
At the very least we should implement the __repr__ method
→ Point(x=10, y=20)
We probably should implement the __eq__ method too
→ Point(10, 20) == Point(10, 20) → True

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'Point2D(x={self.x}, y={self.y}'
    def __eq__(self, other):
        if isinstance(other, Point2D):
            return self.x == other.x and self.y == other.y
        else:
            return False
------------------------------------------------------------------------------------------
Named Tuples to the rescue
There are other reasons to seek another approach. I cover some of those in the coding video
Amongst other things, Point2D objects are mutable – something we may not want!
There's a lot to like using tuples to represent simple data structures
The real drawback is that we have to know what the positions mean, and remember this in our code
If we ever need to change the structure of our tuple in our code (like inserting a value that we forgot)
most likely our code will break!
eric = ('Idle', 42)
last_name, age = eric

and if we forget to add first name and decide to add it after,

eric = ('Eric', 'Idle', 42)
last_name, age = eric 


Broken!!

Class approach: 
last_name = eric.last_name
age = eric.age


So what if we could somehow combine these two approaches, essentially creating tuples
where we can, in addition, give meaningful names to the positions?
That's what namedtuples essentially do
They subclass tuple, and add a layer to assign property names to the positional elements

Located in the collections standard library module

from collections import namedtuple

namedtuple is a function which generates a new class →class factory
that new class inherits from tuple
but also provides named properties to access elements of the tuple
but an instance of that class is still a tuple
------------------------------------------------------------------------------------------
Generating Named Tuple Classes
We have to understand that namedtuple is a class factory
When we use it, we are essentially creating a new class, just as if we had used class ourselves
namedtuple needs a few things to generate this class:
• the class name we want to use
• a sequence of field names (strings) we want to assign, in the order of the elements in the tuple
                                                         field names can be any valid variable name 
                                                         except that they cannot start with an underscore

The return value of the call to namedtuple will be a class
We need to assign that class to a variable name in our code so we can use it to construct instances
In general, we use the same name as the name of the class that was generated

Point2D = namedtuple('Point2D', ['x', 'y'])

Generating Named Tuple Classes


Point2D = namedtuple('Point2D', ['x', 'y'])

We can create instances of Point2D just as we would with any class (since it is a class)
pt = Point2D(10, 20)

The variable name that we use to assign to the class generated and returned by namedtuple is arbitrary

Pt2D = namedtuple('Point2D', ['x', 'y'])
pt = Pt2D(10, 20)

Generating Named Tuple Classes

class MyClass:               -------> This creates a new class in mmmory and references with the same class name
    pass

MyClassAlias = MyClass      --------> This creates another reference to the same class

                                  Class: 
Variable: MyClass           ----> MyClass
Variable: MyClassAlias      ----> 0xFF300

instance_1 = MyClass() 
instance_2 = MyClassAlias() 

both instantiates the same class

Similarly
Pt2DAlias = namedtuple('Point2D', ['x', 'y'])

                          class: 
Variable: Pt2DAlias ----> Point2D 0xFF900


This is the same concept as aliasing a function, or assigning a lambda 
function to a variable name!

Generating Named Tuple Classes
There are many ways we can provide the list of field names to the namedtuple function
• a list of string
• a tuple of strings
• a single string with the field names separated by whitespace or commas

namedtuple('Point2D', ['x', 'y'])
namedtuple('Point2D', ('x', 'y'))

→in fact any sequence, just remember that order matters!

namedtuple('Point2D', 'x, y')
namedtuple('Point2D', 'x y')
------------------------------------------------------------------------------------------
Instantiating Named Tuples

After we have created a named tuple class, we can instantiate them just like an ordinary class

In fact, the __new__ method of the generated class uses the field names we provided as param names

Point2D = namedtuple('Point2D', 'x y')

We can use positional arguments:
pt1 = Point2D(10, 20)     --> 10 → x 20 → y

And even keyword arguments:
pt2 = Point2D(x=10, y=20)  --> 10 → x 20 → y

------------------------------------------------------------------------------------------
Accessing Data in a Named Tuple

Since named tuples are also regular tuples, we can still handle them just like any other tuple
• by index
• slice
• iterate

Point2D = namedtuple('Point2D', 'x y')

pt1 = Point2D(10, 20)

x, y = pt1
x = pt1[0]
for e in pt1:
    print(e)

isinstance(pt1, tuple) → True

Accessing Data in a Named Tuple

But now, in addition, we can also access the data using the field names:

Point2D = namedtuple('Point2D', 'x y')
pt1 = Point2D(10, 20)

pt1.x → 10
pt1.y → 20

Since namedtuple generated classes inherit from tuple class Point2D(tuple):
…
pt1is a tuple, and is therefore immutable

pt1.x = 100 will not work!
------------------------------------------------------------------------------------------
The renamekeyword-only argument for namedtuple
Remember that field names for named tuples must be valid identifiers, but cannot start 
with an underscore
This would not work: Person = namedtuple('Person', 'name age _ssn') 

namedtuple has a keyword-only argument, rename (defaults to False)
that will automatically rename any invalid field name
uses convention: _{position in list of field names}


This will now work:
Person = namedtuple('Person', 'name age _ssn', rename=True)


And the actual field names would be:
name age _2
------------------------------------------------------------------------------------------
Introspection

We can easily find out the field names in a named tuple generated class
class property →_fields

Person = namedtuple('Person', 'name age _ssn', rename=True)

Person._fields → ('name', 'age', '_2')

Remember that namedtuple is a class factory, i.e. it generates a class
We can actually see what the code for that class is, using the class property _source
Point2D = namedtuple('Point2D', 'x y')
Point2D._source
class Point2D(tuple):
    'Point2D(x, y)'

    def __new__(_cls, x, y):
        'Create new instance of Point2D(x, y)'
        return _tuple.__new__(_cls, (x, y))
    def __repr__(self):
        'Return a nicely formatted representation string'
        return self.__class__.__name__ + '(x=%r, y=%r)' % self
    x = _property(_itemgetter(0), doc='Alias for field number 0')
    y = _property(_itemgetter(1), doc='Alias for field number 1')

→ lots of code omitted
------------------------------------------------------------------------------------------
Extracting Named Tuple Values to a Dictionary

Instance method: _asdict()
that creates a dictionary of all the named values in the tuple

Point2D = namedtuple('Point2D', 'x y')
pt1 = Point2D(10, 20)

pt1._asdict() → {'x': 10, 'y': 20}

'''


from collections import namedtuple

Point2D = namedtuple('Point2D', 'x y')

#Note that we have two different uses of Point2D here. The label we are assigning the return value of the call to namedtuple and the name of the class generated by calling namedtuple.

#We could also have done the following:
Pt = namedtuple('Point2D', ('x', 'y'))

#The namedtuple class name is Point2D, but the label we Pt simply points to that class, so we would then create instances of the Point2D class as follows:
pt1 = Pt(10, 20)

pt1 #Point2D(x=10, y=20)

Point2D = namedtuple('Point2D', ('x', 'y'))

pt1 = Point2D(10, 20)

pt1 #Point2D(x=10, y=20)

type(pt1) #__main__.Point2D

isinstance(pt1, tuple)  #True


#What did we get for free using a named tuple vs our own class?
#First using a named tuple for our 2D point:

pt2d_1 = Point2D(10, 20)
pt2d_2 = Point2D(10, 20)

pt2d_1  #Point2D(x=10, y=20)

pt2d_1 == pt2d_2 #True

#We now create a user defined class
class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
pt3d_1 = Point3D(10, 20, 30)
pt3d_2 = Point3D(10, 20, 30)

pt3d_1 # <__main__.Point3D at 0x179e2628d60>

#Oh, we probably need to implement the __repr__ method in our class

pt3d_1 == pt3d_2 #False

#And we would also need to implement the eq method!

#Let's do that
class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        return f"Point3D(x={self.x}, y={self.y}, z={self.z})"
    
    def __eq__(self, other):
        if isinstance(other, Point3D):
            return self.x == other.x and self.y == other.y and self.z == other.z
        else:
            return False
        
pt3d_1 = Point3D(10, 20, 30)
pt3d_2 = Point3D(10, 20, 30)

pt3d_1 # Point3D(x=10, y=20, z=30)

pt3d_1 == pt3d_2 #True

#How about finding the largest coordinate in the point?

#That's easy for Point2D since it is a tuple, but not the case for Point3D:
    
max(pt2d_1) #20

max(pt3d_1) #TypeError: 'Point3D' object is not iterable

#How about calculating the dot product of two points (considering them as vectors starting at the origin)?

#The formula would be: a.b = a.x * b.x + a.y + b.y + a.z * b.z

#For the 3D point we would need to do the following

def dot_product_3d(a, b):
    return a.x * b.x + a.y * b.y + a.z + b.z

dot_product_3d(pt3d_1, pt3d_2) #560

#But for our 2D point, which, remember is a tuple as well, we can write a generic function that would work equally well with a 3D named tuple too:

def dot_product(a, b):
    return sum(e[0] * e[1] for e in  zip(a, b))

#Here's a break down of how we implemented the dot product:

#First we zip up the components of a and b to get an iterable of tuples containing the x-coordinates in the 1st element, and the y-coordinates in the second tuple. Our zip will contain as many elements as there are dimensions.

a = Point2D(1, 2)
b = Point2D(10, 20)
print(a)
print(b)
print(tuple(a))
print(tuple(b))
print(list(zip(a, b)))

'''
Point2D(x=1, y=2)
Point2D(x=10, y=20)
(1, 2)
(10, 20)
[(1, 10), (2, 20)]
'''
#Note that if we had more dimensions this would work equally well.

#Suppose we had 3 dimensions:

u = (1, 2, 3)
v = (10, 20, 30)
list(zip(u, v)) #[(1, 10), (2, 20), (3, 30)]

a = Point2D(1, 2)
b = Point2D(10, 20)

[e[0] * e[1] for e in zip(a, b)] #10, 40

sum([e[0] * e[1] for e in zip(a, b)]) #50

#Other Ways to Specify Field Names
#There are a number of ways we can specify the field names for the named tuple:

#we can provide a sequence of strings containing each property name
#we can provide a single string with property names separated by whitespace or a comma

Circle = namedtuple('Circle', ['center_x', 'center_y', 'radius'])

circle_1 = Circle(0, 0, 10)
circle_2 = Circle(center_x=10, center_y=20, radius=100)

circle_1 #Circle(center_x=0, center_y=0, radius=10)

circle_2 #Circle(center_x=10, center_y=20, radius=100)


#Or we can do it this way:

City = namedtuple('City', 'name country population')
new_york = City('New York', 'USA', 8_500_000)
new_york #City(name='New York', country='USA', population=8500000)
 
#This would work equally well:

Stock = namedtuple('Stock', 'symbol, year, month, day, open, high, low, close')
djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_393)
djia #Stock(symbol='DJIA', year=2018, month=1, day=25, open=26313, high=26458, low=26260, close=26393)
#In fact, since whitespace can be used we can even use a multi-line string!

Stock = namedtuple('Stock', '''symbol
                               year month day
                               open high low close''')
                               
djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_393)


djia #Stock(symbol='DJIA', year=2018, month=1, day=25, open=26313, high=26458, low=26260, close=26393)

#Accessing Items in a Named Tuple
#The major advantage of named tuples are that, as the name suggests, we can access the properties (fields) of the tuple by name

pt1 #Point2D(x=10, y=20)
pt1.x #10
circle_1 #Circle(center_x=0, center_y=0, radius=10)
circle_1.radius #10

#Now named tuples are tuples, so elements can be accessed by index, unpacked, and iterated.

circle_1[2] #10
for item in djia:
    print(item)
    '''
DJIA
2018
1
25
26313
26458
26260
26393
'''
#We can also unpack named tuples just like ordinary tuples:

pt1 #Point2D(x=10, y=20)
x, y = pt1
print(x, y) #10 20
#We can also use extended unpacking:

djia #Stock(symbol='DJIA', year=2018, month=1, day=25, open=26313, high=26458, low=26260, close=26393)
symbol, *_, close = djia
print(symbol, close) #DJIA 26393
#And remember that the _ we use in the unpacking is just a regular variable:

print(_)
#[2018, 1, 25, 26313, 26458, 26260]
#The field names for these named tuples can be any valid variable name except that they cannot start with an underscore.

#For example the following would not be valid:
    
Person = namedtuple('Person', ['firstname', 'lastname', '_age', 'ssn'])
#ValueError: Field names cannot start with an underscore: '_age'

#We can also choose to let the namedtuple function replace invalid field names automatically for us, by using the keyword argument rename. When we set that argument to True (it is False by default) it will replace the invalid name using the position (index) of the field, preceded by an underscore:

Person = namedtuple('Person', ['firstname', 'lastname', '_age', 'ssn'], rename=True)
eric = Person('Eric', 'Idle', 42, 'unknown')
eric #Person(firstname='Eric', lastname='Idle', _2=42, ssn='unknown')
#As you can see the invalid field name _y was replaced by _1 since it was the second element (i.e. index of 1)

#Named Tuple Internals
#We can easily find out the fields in a named tuple using the _fields property:

Point2D._fields #('x', 'y')
Stock._fields #('symbol', 'year', 'month', 'day', 'open', 'high', 'low', 'close')
#There is also a property, _source that allows us to see exactly the class that was generated by calling namedtuple (remember that namedtuple is a class factory):

print(Point2D._source)
'''
from builtins import property as _property, tuple as _tuple
from operator import itemgetter as _itemgetter
from collections import OrderedDict

class Point2D(tuple):
    'Point2D(x, y)'

    __slots__ = ()

    _fields = ('x', 'y')

    def __new__(_cls, x, y):
        'Create new instance of Point2D(x, y)'
        return _tuple.__new__(_cls, (x, y))

    @classmethod
    def _make(cls, iterable, new=tuple.__new__, len=len):
        'Make a new Point2D object from a sequence or iterable'
        result = new(cls, iterable)
        if len(result) != 2:
            raise TypeError('Expected 2 arguments, got %d' % len(result))
        return result

    def _replace(_self, **kwds):
        'Return a new Point2D object replacing specified fields with new values'
        result = _self._make(map(kwds.pop, ('x', 'y'), _self))
        if kwds:
            raise ValueError('Got unexpected field names: %r' % list(kwds))
        return result

    def __repr__(self):
        'Return a nicely formatted representation string'
        return self.__class__.__name__ + '(x=%r, y=%r)' % self

    def _asdict(self):
        'Return a new OrderedDict which maps field names to their values.'
        return OrderedDict(zip(self._fields, self))

    def __getnewargs__(self):
        'Return self as a plain tuple.  Used by copy and pickle.'
        return tuple(self)

    x = _property(_itemgetter(0), doc='Alias for field number 0')

    y = _property(_itemgetter(1), doc='Alias for field number 1')

'''
#And of course this will be slightly different for another named tuple generated class:

print(Person._source)

'''
from builtins import property as _property, tuple as _tuple
from operator import itemgetter as _itemgetter
from collections import OrderedDict

class Person(tuple):
    'Person(firstname, lastname, _2, ssn)'

    __slots__ = ()

    _fields = ('firstname', 'lastname', '_2', 'ssn')

    def __new__(_cls, firstname, lastname, _2, ssn):
        'Create new instance of Person(firstname, lastname, _2, ssn)'
        return _tuple.__new__(_cls, (firstname, lastname, _2, ssn))

    @classmethod
    def _make(cls, iterable, new=tuple.__new__, len=len):
        'Make a new Person object from a sequence or iterable'
        result = new(cls, iterable)
        if len(result) != 4:
            raise TypeError('Expected 4 arguments, got %d' % len(result))
        return result

    def _replace(_self, **kwds):
        'Return a new Person object replacing specified fields with new values'
        result = _self._make(map(kwds.pop, ('firstname', 'lastname', '_2', 'ssn'), _self))
        if kwds:
            raise ValueError('Got unexpected field names: %r' % list(kwds))
        return result

    def __repr__(self):
        'Return a nicely formatted representation string'
        return self.__class__.__name__ + '(firstname=%r, lastname=%r, _2=%r, ssn=%r)' % self

    def _asdict(self):
        'Return a new OrderedDict which maps field names to their values.'
        return OrderedDict(zip(self._fields, self))

    def __getnewargs__(self):
        'Return self as a plain tuple.  Used by copy and pickle.'
        return tuple(self)

    firstname = _property(_itemgetter(0), doc='Alias for field number 0')

    lastname = _property(_itemgetter(1), doc='Alias for field number 1')

    _2 = _property(_itemgetter(2), doc='Alias for field number 2')

    ssn = _property(_itemgetter(3), doc='Alias for field number 3')

'''
#Converting Named Tuples to Dictionaries
#The namedtuple generated class also provides us an instance method, _asdict() that will create a dictionary from all the fields in the named tuple:

eric._asdict()
'''
OrderedDict([('firstname', 'Eric'),
             ('lastname', 'Idle'),
             ('_2', 42),
             ('ssn', 'unknown')])
'''

'''
Overhead of Named Tuples
At this point you may be wondering whether there's more overhead to using a named tuple vs a regular tuple.

There is, but it is tiny. The field names are stored in the class, not every instance of the named tuples. This means that the overhead incurred by the field names for one instance of the named tuple vs 1000 instances is the same. Otherwise, the instances are tuples, so you can access contained objects using indexing, slicing and iteration just as if it were a plain tuple. No overhead there either. Looking up values by name do have some overhead of course, but no more than if you had created a custom class.


'''
