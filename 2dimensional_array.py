###########################################################
##### Assignment 3 Section 1

###########################################################

import numpy as np
import prettytable
from numpy.ma.extras import column_stack

table = prettytable.PrettyTable()

table.add_column('North',['Bob', 'Stef', 'Ron'])
table.add_column('South', ['Sue', 'Janice', 'Will'])
table.add_column('East',['Nathan', 'Henry', 'Kimmy'])
table.add_column('West',['Wonda', 'Charles', 'Pete'])
print('Section 1: Two-dimensional NumPy Array')
print(table)

###########################################################
##### Assignment 3 Section 2

###########################################################

salesTeam = ['Bob', 'Stef', 'Ron']

print('\nSection 2: NumPy Array')
print(f'There are {np.array(len(salesTeam))} in the NumPy array')

result = np.isin('Stef', salesTeam)
if result == True:
    print('Stef is in the salesTeam NumPy array')
else:
    print('Stef is not in the salesTeam NumPy array')

south_index = table.field_names.index('South')
south_col = [row[south_index] for row in table.rows]
combined = south_col + salesTeam
print(f'There are {len(combined)} in the NumPy array')

combined.remove('Janice')
combined.remove('Ron')
print(f"There are {len(combined)} in the NumPy array")

print("Names currently in the SalesTeam NumPy array")
for item in combined:
    print(item)

