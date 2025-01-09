#//*********************************************************

#//****Assignment 6 Section 1

#//*********************************************************

print(f'Assignment 6 – Asserts and Try/Except\n\nSection 1\n')

def validate_value(j, k):
  try:
    # Check if the value is empty
    assert j is not None and j != '', 'Parameter must not be empty or null.\n'
  except AssertionError as e:
    print(e)

  try:
    # Check if the value is greater than 0
    assert k > 0, 'Parameter must be greater than zero.\n'

  except AssertionError as e:
    print(e)
    
validate_value(j='', k=0)   


#//*********************************************************

#//****Assignment 6 Section 2

#//*********************************************************

print(f'Section 2\n')

string_arrays = ['john', 'nola', 'sadie', 'whiskey', 'kenz']

def out_of_bounds(list):
  try:
    for item in range(len(list) + 1):
      _ = list[item]
  except IndexError:
    print('Array out of bounds error occurred.\n')

out_of_bounds(string_arrays)

#//*********************************************************

#//****Assignment 6 Section 3

#//*********************************************************

print(f'Section 3\n')

def missing_file(file):
  try:
    open(file)
  except FileNotFoundError:
    print('File not found error.\n')
missing_file('NoFileNamedThis.txt')

#//*********************************************************

#//****Assignment 6 Section 4

#//*********************************************************

print(f'Section 4\n')

number = [1, 0]

def divideByZero(number):
  try:
      for divisor in number:
        if divisor != 0:
          pass
        if divisor == 0:
           raise ZeroDivisionError
  except ZeroDivisionError as e:
    print(f'Divide by zero error occurred.\n')
    print('Divide by Zero.')

divideByZero(number)


