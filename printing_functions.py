# Chapter 8 , Question no.8-15. Printing Models:
import print_models

print_models.sandwich('vegetables','cheese','mayo')

print('\n')
# Chapter 8 , Question no.8-16. Imports:
#import module_name

import print_models

print_models.make_shirt('Medium','Python is awesome!!!')

#from module_name import function_name

from print_models import sandwich

sandwich('Chicken','Tomatoes')

print('\n')
#from module_name import function_name as fn

from print_models import make_shirt as ms

ms('Large','You are Superb!')
print('\n')

#import module_name as mn

import print_models as pm

pm.sandwich('Tikka','Cucumber','Mayo')
print('\n')

#from module_name import *

from print_models import *

sandwich('Fajita','Olives')

