'''
Named tuples - Modifying and Extending

Named Tuples are Immutable

So how can we "change" one or more values inside the tuple?

Just like with strings, we have to create a new tuple, with the modified values

Point2D = namedtuple('Point2D', 'x y')
pt = Point2D(0, 0)

Suppose we need to change the value of the x coordinate:

Simple approach: pt = Point2D(100, pt.y)

Note that the memory address of pt has now changed

Drawback
This simple approach can work well, but it has a major drawback

Stock = namedtuple('Stock', 'symbol year month day open high low close')
djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_393)

Suppose we only want to change the closefield

djia = Stock(djia.symbol, 
             djia.year, 
             djia.month, 
             djia.day,           painful!
             djia.open, 
             djia.high, 
             djia.low, 
             26_394)

----------------------------------------------------------------------------------
Maybe slicing or unpacking?

djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_393)

current = djia[:7] current →('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260)

*current, _ = djia current →['DJIA', 2018, 1, 25, 26_313, 26_458, 26_260]

djia = Stock(*current, 26_394)

We can also use the _make class method – but we need to create an iterable that contains all 
the values first:
    
new_values = current + (26_394,)    new_values = current.append(26_394)
new_values →'DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_394


djia = Stock._make(new_values) { new_values -> iterable}
----------------------------------------------------------------------------------
This still has drawbacks

djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_393)

What if we wanted to change a value in the middle, say day?

Cannot use extended unpacking (only one starred value in extending unpacking)
*pre, day, *post = djia makes no sense…

Slicing will work: pre = djia[:3]
                         post = djia[4:]

new_values = pre + (26,) + post
new_values →('DJIA', 2018, 1, 26, 26_313, 26_458, 26_260, 26_394)

djia = Stock(*new_values)
----------------------------------------------------------------------------------
But even this still has drawbacks!

djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_393)

How about modifying both the day and the highvalues?

new_values = djia[:3] + (26,) + djia[4:5] + (26_459,) + djia[6:]

djia = Stock(*new_values) 

This is just unreadable and extremely error prone!

There has to be a better way!
----------------------------------------------------------------------------------
The _replace instance method

Named tuples have a very handy instance method, _replace
It will copy the named tuple into a new one, replacing any values from keyword arguments
The keyword arguments are simple the field names in the tuple and the new value
The keyword name must match an existing field name

Stock = namedtuple('Stock', 'symbol year month day open high low close')
djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_393)

djia = djia._replace(day=26, high=26_459, close=26_394)

djia → 'DJIA', 2018, 1, 26, 26_313, 26_459, 26_260, 26_394

Note that the memory address of djiahas now changed
----------------------------------------------------------------------------------
Extending a Named Tuple

Sometimes we want to create named tuple that extends another named tuple, appending one 
or more fields

Stock = namedtuple('Stock', 'symbol year month day open high low close')

We want to create a new named tuple class, StockExt that adds a single field, previous_close

When dealing with classes, this is sometimes done by using subclassing.

But this not easy to do with named tuples

and there's a cleaner way of doing it anyway


Extending a Named Tuple

Point2D = namedtuple('Point2D', 'x y')

Let's say we want to create a Point3D named tuple that has an extra parameter

Yes, the obvious, and simplest approach here is best:
Point3D = namedtuple('Point3D', 'x y z')

But what happens if you have a lot of fields in the named tuple? Code is not as clean anymore…

Stock = namedtuple('Stock', 'symbol year month day open high low close')

StockExt = namedtuple('Stock', 'symbol year month day open high low close previous_close')

How about re-using the existing field names in Stock?


Extending a Named Tuple

Stock = namedtuple('Stock', 'symbol year month day open high low close')

Stock._fields →'symbol', 'year', 'month', 'day', 'open', 'high', 'low', 'close'

We can then create a new named tuple by "extending" the _fields tuple

new_fields = Stock._fields + ('previous_close', )
StockExt = namedtuple('StockExt', new_fields)


Extending a Named Tuple

We can also easily use an existing Stockinstance to create a new StockExt instance
with the same common values, adding in our new previous_close value:
Stock = namedtuple('Stock', 'symbol year month day open high low close')

djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_393)

StockExt = namedtuple('StockExt', Stock._fields + ('previous_close', )

djia_ext = StockExt(*djia, 26_000)

or
djia_ext = StockExt._make(djia + (26_000, ))
----------------------------------------------------------------------------------

'''
from collections import namedtuples

Point2D = namedtuples('Point2D', 'x y')

pt = Point2D(10,20)
pt #Point2D(x=10, y=20)
id(pt) 1623001915328

pt.x = 100 #AttributeError: can't set attribute
#coz we it is tuple

pt = Point2D(100,pt.y)
pt #Point2D(x=100, y=20)
id(pt) #1623001492800

#Id got changed that means pt is referencing to new memory locations
# we are overwriting

Stock = namedtuple('Stock', 'symbol year month day open high low close')

djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_393)

#To update the close property for example, we could write

djia = Stock(djia.symbol, djia.year, djia.month, djia.day, 
                  djia.open, djia.high, djia.low, 26_394)

#Now that was quite painful!

#We can be a bit more clever about this and use tuple unpacking and argument unpacking as follows

*values, _ = djia

values #['DJIA', 2018, 1, 25, 26313, 26458, 26260]

values.append(26_456)

djia = Stock(*values)

djia  #Stock(symbol='DJIA', year=2018, month=1, day=25, open=26313, high=26458, low=26260, close=26456)

'''
This is much better than our first attempt!

But this approach does not always work, what happens if we want to change a values somewhere in the middle? Or two values?

We cannot do: *first, month, *last = djia

That would make no sense whatsoever! (and Python will tell you so!)

Maybe slicing and unpacking can work here...
'''

djia #Stock(symbol='DJIA', year=2018, month=1, day=25, open=26313, high=26458, low=26260, close=26393)
#We could try slicing:

djia[:3] #('DJIA', 2018, 1)
djia[:3] + (26,) + djia[4:] #('DJIA', 2018, 1, 26, 26313, 26458, 26260, 26393)
#So now we could use this to create a new StockPrice instance:

djia2 = Stock(*(djia[:3] + (26,) + djia[4:]))
djia2 #Stock(symbol='DJIA', year=2018, month=1, day=26, open=26313, high=26458, low=26260, close=26393)
#This works, but that's quite cumbersome...
#And it gets worse - suppose we want to modify the year and day using this approach:


djia #Stock(symbol='DJIA', year=2018, month=1, day=25, open=26313, high=26458, low=26260, close=26393)

values = djia[0:1] + (2019,) + djia[2:3] + (26,) + djia[4:]

values #('DJIA', 2019, 1, 26, 26313, 26458, 26260, 26393)

djia = Stock(*values)

djia #Stock(symbol='DJIA', year=2018, month=1, day=25, open=26313, high=26458, low=26260, close=26456)

#Or, if you want to avoid unpacking the values into the multiple positional arguments required by the Stock constructor, we can make us of the _make class method that can use an iterable:

djia4 = Stock._make(values)
djia4 #Stock(symbol='DJIA', year=2019, month=1, day=26, open=26313, high=26458, low=26260, close=26393)
#This is really getting too complex.

#Fortunately there's a better way!

#The namedtuple implementation also provides another instance method called _replace which takes keyword-only arguments. That method will make a copy of the current tuple and substitute property values based on the keyword-only arguments passed in.

djia #Stock(symbol='DJIA', year=2018, month=1, day=25, open=26313, high=26458, low=26260, close=26393)
id(djia)
2785020879400

djia5 = djia._replace(year=2019, day=26)
djia5 #Stock(symbol='DJIA', year=2019, month=1, day=26, open=26313, high=26458, low=26260, close=26393)
djia #Stock(symbol='DJIA', year=2018, month=1, day=25, open=26313, high=26458, low=26260, close=26393)
id(djia5) #2785020880480
#Much better!!

#Extending Named Tuples
#Sometimes we may want to add one or more properties to an existing class without modifying the code for the custom class itself.

#Using inheritance is one way to go about it so you may be tempted to do this with named tuples as well, but it's not easy, and there's a cleaner way to do this if all you're after is additional data fields.

#Let's say we have a Point class that is for 2D problems:

Point2D = namedtuple('Point2D', 'x y')
#We could easily create a 3D point class as follows:

Point3D = namedtuple('Point3D', 'x y z')
#But if our named tuple has many fields, such as our Stock named tuple that's a little more difficult:

djia #Stock(symbol='DJIA', year=2018, month=1, day=25, open=26313, high=26458, low=26260, close=26393)
#Suppose we want to create a new class, say StockExt, it would take some effort:

StockExt = namedtuple('StockExt', 
                      '''symbol year month day open high low 
                      close previous_close''')
#Instead we can leverage that _fields property:

Stock._fields
#('symbol', 'year', 'month', 'day', 'open', 'high', 'low', 'close')
#Remember that the namedtuple initializer can handle a list or tuple containing the field names. For example, the one we just retrieved from _fields.

#Now all we need to do is create a new tuple that contains those fields along with whatever extras we want:

new_fields = Stock._fields + ('previous_close',)
new_fields 
'''
('symbol',
 'year',
 'month',
 'day',
 'open',
 'high',
 'low',
 'close',
 'previous_close')
'''
#And now we can create our new named tuple this way:

StockExt = namedtuple('StockExt', Stock._fields + ('previous_close',))
StockExt._fields
'''
('symbol',
 'year',
 'month',
 'day',
 'open',
 'high',
 'low',
 'close',
 'previous_close')
'''
#If you did not want to use tuple concatenation for some reason, you could also do it using strings:

' '.join(Stock._fields) + ' previous_close' #'symbol year month day open high low close previous_close'
StockExt = namedtuple('StockExt', 
                      ' '.join(Stock._fields) + ' previous_close')

StockExt._fields
'''
('symbol',
 'year',
 'month',
 'day',
 'open',
 'high',
 'low',
 'close',
 'previous_close')
'''
#Now, with this newly extended class, we may want to take one of the "old" named tuple instance (djia) and create the extended version of it using the StockExt class.

#This is also quite simple to do, since named tuples are tuples, and can therefore be unpacked in the arguments of a function call.

djia #Stock(symbol='DJIA', year=2018, month=1, day=25, open=26313, high=26458, low=26260, close=26393)
djia_ext = StockExt(*djia, 25_000)
djia_ext #StockExt(symbol='DJIA', year=2018, month=1, day=25, open=26313, high=26458, low=26260, close=26393, previous_close=25000)
#or, we can use the _make method:

djia_ext = StockExt._make(djia + (25_000, ))
djia_ext #StockExt(symbol='DJIA', year=2018, month=1, day=25, open=26313, high=26458, low=26260, close=26393, previous_close=25000)

