import sys
import logging

# docs
# https://docs.python.org/3/library/logging.handlers.html

print('Assignment 7 – Logging Exceptions to a File.')
print('\nTesting Try/Except for Divide by Zero, File Does Not Exist, Array Out of Bounds, and Array is Null scenarios.')
print('\nAll console error messages are printed from error log file.')

# Logging to a file.

log_file = "stderr_log.txt"
logging.basicConfig(
    filename=log_file,
    level=logging.ERROR,
    format="ERROR:root%(message)s",

)

# Redirecting sys.stderr to the file
sys.stderr = open(log_file, 'a')


# Read the log file and display to the console
def displayLogfile(logs):
  with read(logs, 'r') as file:
    contents = file.read(logs)
  print('Show the contents of the log file.')
  print(contents)
 

# Divide a number by 0
def divideByZero(number):
  33 / number
  raise ZeroDivisionError("Attempted to divide by zero.") 
   


# fileDoesNotExist function

def fileDoesNotExist(filename):
  with read(filename, 'r') as file:
    file_contents = file.read(filename)
  raise FileNotFoundError("Could not find file NoFileNamedThis.txt.")


# Array OutOfbound
def arrayOutOfBounds(name):
  bounds = [ "out", "of", "boundz"]
  for item in name[6]:
    print(item)
  raise IndexError("Index was outside the bounds of the array.")
  

# Nullarray
def arrayIsNull():
  my_array = []
  my_array = list()
  print(my_array)
  raise ValueError("Object reference not set to an instance of an object.")


# Calling all functions

try:
    divideByZero()
except ZeroDivisionError as e:
    logging.error(e)

try:
    fileDoesNotExist()
except FileNotFoundError as e:
    logging.error(e)

try:
    arrayOutOfBounds()
except IndexError as e:
    logging.error(e)

try:
    arrayIsNull()
except ValueError as e:
    logging.error(e)

# Display the log file contents
displayLogfile(log_file)
