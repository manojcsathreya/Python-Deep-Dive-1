import sys
#whwere does it get sys from?
sys #<module 'sys' (built-in)>

import collections 
collections #<module 'collections' from 'C:\\Users\\Manoj.Sathish\\Anaconda3\\lib\\collections\\__init__.py'>

#can we do this?
mod_name = 'math'
import mod_name #ModuleNotFoundError: No module named 'mod_name'
#we cannot. We cannot have a variable having module name and then importing it
#instead we can use import lib

import importlib
importlib #<module 'importlib' from 'C:\\Users\\Manoj.Sathish\\Anaconda3\\lib\\importlib\\__init__.py'>

importlib.import_module(mod_name) #<module 'math' (built-in)>

'math' in sys.modules #True

'fractions' in sys.modules #True

#well can we use it now?

math.sqrt(2) #NameError: name 'math' is not defined
# What just happened?
'math' in globals() #False

#what importlib did was it just created an object in sys cache so we have to create a reference for it
math = sys.modules['math']
math.sqrt(2) #1.4142135623730951
'math' in globals() #True

#or we can do
mod_name = 'math'
math2 = importlib.import_module(mod_name)
'math2' in globals() #True

id(math) #2379018991312
id(math2) #2379018991312
id(sys.modules['math']) #2379018991312

'''
What happens when we import the modules?
well, it  comprises of two things 1. finder 2. Loader
finder+loader = import
when ever interpreter encounters import it askes finders about the module info
finders might know where the modules are located, and if they find any, they'll return loaders to interpreter
loaders then complies, executes the module and brings the reference to global name space
Finder returns a module specification file
'''
import math

math.__spec__ #ModuleSpec(name='math', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')

#finders
sys.meta_path
'''
[_frozen_importlib.BuiltinImporter,
 _frozen_importlib.FrozenImporter,
 _frozen_importlib_external.PathFinder,
 <six._SixMetaPathImporter at 0x229edc4e1f0>]
'''

#we can find the loaders 
importlib.util.find_spec('decimal')#ModuleSpec(name='decimal', loader=<_frozen_importlib_external.SourceFileLoader object at 0x00000229EE2BB250>, origin='C:\\Users\\Manoj.Sathish\\Anaconda3\\lib\\decimal.py')

#writing a new file into same directory
with open('module1.py','w') as code_file:
    code_file.write("print('running module1.py.....')\n")
    code_file.write("a=100")
    
importlib.util.find_spec('module1')#ModuleSpec(name='module1', loader=<_frozen_importlib_external.SourceFileLoader object at 0x00000229F0C58670>, origin='C:\\Users\\Manoj.Sathish\\module1.py')

import module1#running module1.py.....

module1.a#100

import os 

ext_file_source = os.environ['HOMEPATH']
ext_file_source#'\\Users\\Manoj.Sathish'
file_abs_path = os.path.join(ext_file_source,'module2.py')
with open('module2.py','w') as code_file:
    code_file.write("print('running module2.py.....')\n")
    code_file.write("x = 'python'")
importlib.util.find_spec('module2')

    
import module2

