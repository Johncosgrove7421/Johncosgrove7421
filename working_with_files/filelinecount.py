import pandas as pd
import numpy as np
#//*********************************************************

#//****Assignment 5 Section 1

#//*********************************************************

print('Section 1') # Add the following data to the produce dictionary by adding key names as Fruit and Price.

produceDict = pd.DataFrame({'Fruit': ['bananas', 'grapes', 'apples', 'pears', 'lettuce', 'onions', 'potatoes', 'peaches'], 'Price': [0.59, 2.99, 1.49, 1.39, 0.99, 0.79, 0.58, 1.59]})
produceDict.to_string('ProducePrice.txt', index=False)

def fileLineCount(file):
  df = pd.read_csv(f'{file}.txt')
  num_rows = df.shape[0]
  print(f'There are {num_rows} in the file, where {num_rows} is the number returned by fileLineCount()')

fileLineCount('ProducePrice')

#//*********************************************************

#//****Assignment 5 Section 2

#//*********************************************************

print('\nSection 2') # add four more items to the produceDict and append them to the ProducePrice.txt file

new_data = {
  'Fruit': ['celery', 'cabbage', 'tomatoes', 'peppers'],
  'Price': [1.29, 0.79, 1.19, 0.99],
}

new_row = pd.DataFrame(new_data)
df = pd.concat([produceDict, new_row])
df = df.reset_index(drop=True)
df.to_string('ProducePrice.txt', index=False)

fileLineCount('ProducePrice')


#//*********************************************************

#//****Assignment 5 Section 3

#//*********************************************************

print('\nSection 3')
producePrices = pd.read_csv(f'ProducePrice.txt')
producePrices = producePrices.reset_index(drop=True)
producePrices.index = np.arange(1, len(producePrices) + 1)
print(producePrices)

fileLineCount('ProducePrice')