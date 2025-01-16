import sys
import logging

# Assignment Header
print("Assignment 7 – Logging Exceptions to a File.")
print("\nTesting Try/Except for Divide by Zero, File Does Not Exist, Array Out of Bounds, and Array is Null scenarios.")
print("\nAll console error messages are printed from error log file.\n")

# Configure logging to write to a file
log_file = "stderr_log.txt"
logging.basicConfig(
    filename=log_file,
    level=logging.ERROR,
    format="ERROR:root:%(message)s",
)

# Redirect sys.stderr to the log file
sys.stderr = open(log_file, 'a')

# Function to display the contents of the log file
def displayLogfile(logs):
    with open(logs, 'r') as file:
        contents = file.read()
    print(contents)

# Divide a number by 0
def divideByZero():
    raise ZeroDivisionError("Attempted to divide by zero.")

# Attempt to open a non-existent file
def fileDoesNotExist():
    raise FileNotFoundError("Could not find file NoFileNamedThis.txt")

# Access an index outside the bounds of an array
def arrayOutOfBounds():
    bounds = ["out", "of", "bounds"]
    raise IndexError("Index was outside the bounds of the array.")

# Access an item in a null (empty) array
def arrayIsNull():
    my_array = []
    if not my_array:
        raise ValueError("Object reference not set to an instance of an object.")

# Test the functions with try/except blocks
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
