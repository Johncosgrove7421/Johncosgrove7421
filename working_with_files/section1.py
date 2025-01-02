import pandas as pd
import numpy as np
import os
#//*********************************************************

#//****Assignment 5 Section 1

#//*********************************************************

print('Section 1')
# Add the following data to the produce dictionary by adding key names as Fruit and Price.

produceDict = pd.DataFrame({'Fruit': ['bananas', 'grapes', 'apples', 'pears', 'lettuce', 'onions', 'potatoes', 'peaches'], 'Price': [0.59, 2.99, 1.49, 1.39, 0.99, 0.79, 0.58, 1.59]})
produceDict.index = np.arange(1, len(produceDict) + 1)
produceDict.to_string('ProducePrice.txt')

def fileLineCount(file):
  df = pd.read_csv(f'{file}.txt')
  num_rows = df.shape[0]
  print(f'There are {num_rows} in the file, where {num_rows} is the number returned by fileLineCount()')

fileLineCount(file='ProducePrice')

#//*********************************************************

#//****Assignment 5 Section 2

#//*********************************************************

print('Section 2')
# add four more items to the produceDict and append them to the ProducePrice.txt file


['peppers', 'celery', 'cabbage', 'tomatoes']
[0.99, 1.29, 0.79, 1.19]


# UPDATE
# print(f'There are {len(produceDict["Fruit"])} in the file, where {len(produceDict["Fruit"])} is the number returned by fileLineCount()')

fileLineCount(file='ProducePrices')

#//*********************************************************

#//****Assignment 5 Section 3

#//*********************************************************

print('Section 3')
produceDict.index = np.arange(1, len(produceDict) + 1)
print(produceDict)
# UPDATE
#print(f'There are {len(produceDict["Fruit"])} in the file, where {len(produceDict["Fruit"])} is the number returned by fileLineCount()')