'''
Tuples vs Lists vs Strings


Tuples                           Lists                            Strings
containers                      containers                        containers
order matters                   order matters                     order matters
Heterogeneous / Homogeneous     Homogeneous / Heterogeneous       Homogeneous
indexable                       indexable                         indexable
iterable                        iterable                          iterable
immutable                       mutable                           immutable 
fixed length                    length can change                 fixed length
fixed order                     order of elements can change      fixed order
cannot do in-place sorts        can do in-place sorts             cannot do in-place sorts
cannot do in-place reversals    can do in-place reversals         cannot do in-place reversals 
-------------------------------------------------------------------------------------------------
Immutability of Tuples

elements cannot be added or removed
the order of elements cannot be changed
works well for representing data structures:

Point: (10, 20)     1st element is the x-coordinate
                    2nd element is the y-coordinate
Circle: (0, 0, 10)  1st element is the x-coordinate of the center
                    2nd element is the y-coordinate of the center
                    3rd element is the radius


City: ('London', 'UK', 8_780_000) 1st element is the name of a city
                                  2nd element is the country
                                  3rd element is the population

The position of the data has meaning

-------------------------------------------------------------------------------------------------
Tuples as Data Records

Think of a tuple as a data record where the position of the data has meaning

london = ('London', 'UK', 8_780_000)
new_york = ('New York', 'USA', 8_500_000)
beijing = ('Beijing', 'China', 21_000_000)

Because tuples, strings and integers are immutable, we are guaranteed
that the data and data structure for london will never change

We can have a list of these tuples:

cities = [('London', 'UK', 8_780_000),
          ('New York', 'USA', 8_500_000),
          ('Beijing', 'China', 21_000_000)]
-------------------------------------------------------------------------------------------------
Extracting data from Tuples
Since tuples are sequences just like strings and lists, we can retrieve items by index
london = ('London', 'UK', 8_780_000)
city = london[0] country = london[1] population = london[2]

cities = [('London', 'UK', 8_780_000),
          ('New York', 'USA', 8_500_000),
          ('Beijing', 'China', 21_000_000)]

total_population = 0
for city in cities:
    total_population += city[2]

You'll notice how the list of cities is homogeneous (contains cities only)
But a city (the tuple) is heterogeneous


Extracting data from Tuples

We can also use tuple unpacking

We actually already know how to do this – we covered this in the section on function arguments
new_york = ('New York', 'USA', 8_500_000)
packed three values into a tuple

city, country, population = new_york
unpacked tuple

city, country, population = ('New York', 'USA', 8_500_000)
city, country, population = 'New York', 'USA', 8_500_000
-------------------------------------------------------------------------------------------------
Dummy Variables
This is something you’re likely to run across when you look at Python code that uses tuple unpacking

Sometimes, we are only interested in a subset of the data fields in a tuple, not all of them

Suppose we are interested only in the city name and the population:

city, _, population = ('Beijing', 'China', 21_000_000)

_is actually a legal variable name – so there's nothing special about it

but by convention, we use the underscore to indicate this is a variable we don't care about

in fact, we could just have used:
    
city, ignored, population = ('Beijing', 'China', 21_000_000)


Dummy Variables
It's also used in extended unpacking too
record = ('DJIA', 2018, 1, 19, 25987.35, 26071.72, 25942.83, 26071.72)
symbol, year, month, day, open, high, low, close = record
Let's say we are only interested in the symbol, year, month, dayand close fields

We could do it this way: symbol = record[0]
year = record[1]
month = record[2]
day = record[3]
close = record[7]

looks really bad!

symbol, year, close = record[0], record[1], record[7]

we can uset this instead

symbol, year, month, day, *_, close = record
symbol, year, month, day, *ignored, close = record
-------------------------------------------------------------------------------------------------

 
'''
'''
Tuples are an immutable container type.

They contain a collection of objects. The tuple is a sequence type - this means order matters (and is preserved) and elements can be accessed by index (zero based), slicing, or iteration.

Other common sequence types in Python include lists and strings. Strings, like tuples are immutable, whereas lists are mutable.

Tuples are sometimes presented as immutable lists, but in fact, they could be compared more closely to strings with one major difference: strings are homogeneous sequences, while tuples can be heterogeneous.

A tuple literal is often presented as:
'
'''
('a', 10, True)

#But the parentheses are not what indicate a tuple - it is the commas:
    
a = ('a', 10, True)
b = 'b', 20, False

type(a)#tuple

type(b)#tuple

#Since tuples are sequence types, we can access items by index:

a = 'a', 10, True
a[2] #True

#Or we can even slice them:
a = 1, 2, 3, 4, 5
a[2:4] #(3, 4)

#We can iterate over them:
    
a = 1, 2, 3, 4, 5
for element in a:
    print(element)
    
'''
1
2
3
4
5
'''
    
#We can also use unpacking:
    
point = 10, 20, 30

x, y, z = point

print(x)
print(y)
print(z)


'''
10
20
30
'''

#Tuples are immutable, in the sense that we cannot change the reference of an object in the container and we cannot add or remove objects from the container. This is the same as strings.

a = 10, 'python', True
a[0] = 20
#TypeError: 'tuple' object does not support item assignment
#We can however 'extend' tuples, but just as with strings, we are actually just creating a new tuple:
a = 1, 2, 3
id(a) #2726988303960

a = a + (4, 5, 6)
a #(1, 2, 3, 4, 5, 6)
id(a) #2726964089000

#As you can see we no longer have the same memory address for a.

#We have to be careful when we think about immutability of tuples. The tuple, as a container is immutable, but the elements contained in the tuple may very well be mutable.

a =([1,2,3],)
print(type(a)) #<class 'tuple'>
a[0][2] = 4
a #([1, 2, 4],)

#to explain this more

#Let's define a simple point class to store the x and y coordinates of a point in 2D space:
    
class Point2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f'{self.__class__.__name__} (x = {self.x}, y= {self.y})'
    
a = Point2D(0, 0), Point2D(10, 10), Point2D(20, 20)
a #(Point2D (x = 0, y= 0), Point2D (x = 10, y= 10), Point2D (x = 20, y= 20))

a[0]= Point2D(-10, -20) #TypeError: 'tuple' object does not support item assignment

#But we can modify the contents of the first element:
a[0].x = -10
a #(Point2D (x = -10, y= 0), Point2D (x = 10, y= 10), Point2D (x = 20, y= 20))

'''
Tuples as Data Records
We can interpret tuples as lightweight data structures where, by convention, the position of the element in the tuple has meaning.

For example, we may elect to represent a point as a tuple, and not use the class approach we just did:
'''
pt1 = (0, 0)
pt2 = (10, 10)

'''
Here, we simply decide that the first position of the tuple represents the x=coordinate while the second element represents the y-coordinate of a point in 2D space.

We could also decide that we are going to represent a city using a tuple, where the first position will the city name, the second position will be the country, and the the third position will be the population:
'''
london = 'London', 'UK', 8_780_000
new_york = 'New York', 'USA', 8_500_000
beijing = 'Beijing', 'China', 21_000_000

cities = london, new_york, beijing

city_names = [t[0] for t in cities]
print(city_names) #['London', 'New York', 'Beijing']

total = 0
for city in cities:
    total += city[2]
print (f'total={total}') #total=38280000

'''
You will note that the reason this worked is because the cities list contained only city tuples. The list was homogeneous. The tuples on the other hand are heterogeneous.

This is often a key difference between lists and tuples, especially when we consider tuples as data structures. The tuples are heterogeneous, while the list needs to be homogeneous so we can apoply the same calculations to each element of the list.

The above example would break if one of the elements in the cities list was an integer for example.

Back to our example calculating the total population. There is a more Pythonic way of doing this.

First we use a comprehension to extract just the population from each city :
'''

[city[2] for city in cities]
#[8780000, 8500000, 21000000]

sum([city[2] for city in cities]) #38280000

record = 'DJIA', 2018, 1, 19, 25_987, 26_072, 25_942, 26_072
#Where the structure is: symbol, year, month, day, open, high low, close

#We could then unpack the record using straight unpacking:
    
symbol, year, month, day, open_, high, low, close = record
print(symbol) #DJIA
print(close) #DJIA

#But suppose we are only interested in the symbol, year, month, day and close. Then we could use extended unpacking as follows:

symbol, year, month, day, *others, close = record

print(symbol, year, month, day, close)

#DJIA 2018 1 19 26072

print(others) #[25987, 26072, 25942]

#A convetion often used in Python when we are not particularly interested in something, is to use an underscore as a variable name:
    
symbol, year, month, day, *_, close = record
#There's nothing special about the underscore here, it's just a legal variable name (in an interactive Python session, the underscore is actually used to store the results of the last calculation)
