import os
import logging

# docs
# https://docs.python.org/3/library/logging.handlers.html

print('Assignment 7 – Logging Exceptions to a File.')
print('\nTesting Try/Except for Divide by Zero, File Does Not Exist, Array Out of Bounds, and Array is Null scenarios.')
print('\nAll console error messages are printed from error log file.')

# Logging to a file.

if (os.path.exists("logFile.txt")):
  os.remove("logFile.txt")

# Logging for standard error

logger = logging.getLogger('')
logging.basicConfig(filename="logFile.txt")
stderrLogger=logging.StreamHandler()
stderrLogger.setFormatter(logging.Formatter(logging.BASIC_FORMAT))
logging.getLogger().addHandler(stderrLogger)

# Open and read log file
def displayLogFile():
  try:
       f = open("logFile.txt", "r")
       print(f.read())
  except:
       print('Failed to read log file')

# Function to divide by zero
def divideByZero():
   x = 33
   y = 0
   if y == 0:
     raise Exception("Attempted to divide by zero.")
   return x/y

# Open a non existant file
def fileDoesNotExist():
   try:
     f = open("NoFileNamedThis.txt", "r")
   except:
     raise Exception("Could not find file NoFileNamedThis.txt")

# Out of Bounds
def arrayOutOfBounds():
   names = ["ed", "john", "kenz", "Mel"]
   someName = []

   # Test and print exception
   try:
        for i in range(0, (len(names) +1)):
            if(i >= len(names)):
                raise Exception("Index was outside the bounds of the array.")
   except Exception as ae:
       raise Exception("Index was outside the bounds of the array")

# null array
def arrayIsNull():
    myArr = []
    try:
        print(myArr[1])
    except Exception as ae:
         raise Exception("Object reference not set to an instance of an object")

# Calling all functions

try:
    divideByZero()
except Exception as ae:
    logger.error(ae)

try:
    fileDoesNotExist()
except Exception as ae:
    logger.error(ae)

try:
    arrayOutOfBounds()
except Exception as ae:
    logger.error(ae)

try:
    arrayIsNull()
except Exception as ae:
    logger.error(ae)

# Display the log file contents
print('\n\nShow the contents of the log file')
displayLogFile()


