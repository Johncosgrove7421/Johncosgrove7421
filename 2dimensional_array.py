###########################################################
##### Assignment 3 Section 1

###########################################################

import numpy as np
import prettytable
from numpy.ma.extras import column_stack

table = prettytable.PrettyTable()

table.field_names = ['North', 'South', 'East', 'West']
table.add_row(['Bob', 'Sue', 'Nathan', 'Wanda'])
table.add_row(['Stef', 'Janice', 'Henry', 'Charles'])
table.add_row(['Ron', 'Will', 'Kimmy', 'Pete'])

print(table)

###########################################################
##### Assignment 3 Section 2

###########################################################

salesTeam = np.array(['Bob', 'Stef', 'Ron'])

# South = (table.get_string(fields=['South']))

result = np.isin('Stef', salesTeam)

print('Section 2: NumPy Array')
print(f'There are {np.array(len(salesTeam))} in the NumPy array')

if result == True:
    print('Stef is in the salesTeam NumPy array')
else:
    print('Stef is not in the salesTeam NumPy array')

# Left of on  section 2 #6


# print(f'There are {(len(table.field_names))} names in the NumPy array')


#      f'There are {} in the NumPy array\n'
#      f'Names currently in the salesTeam NumPy array'

# Expected Output

# There are 6 names in the Numpy array
# There are 4 names in the Numpy array
# Names currently in the salesTeam NumPy array
# Bob
# Stef
# Sue
# Will
