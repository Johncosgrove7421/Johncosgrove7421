#//*********************************************************

# Section 1

carDealz = ['Ford', 'Mustang', '2010'], ['Chevrolet', 'Silverado', '2008'], ['Dodge', 'Charger', '2012']

print('\n\nSection 1: Array of Structures')

for car in carDealz:
	for element in car:
		print(element, end=' ')
	print()

# //*********************************************************

# Section 2

inventoryCount = {'Mustang': '9', 'Silverado': '13', 'Charger': '4'}

print('\n\nSection 2: Inventory Count')

for k,v  in inventoryCount.items():
	print(f'There are {v} {k}')


# //*********************************************************

# Section 3

DaysofWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

print('\n\nSection 3: Days of the Week\n')

print('Days of the week:')
for days in DaysofWeek:
	print(days)

print('\nDays of the week in reverse:')
for days in DaysofWeek[::-1]:
        print(days)

print(f'\nWorkdays are:')
for days in DaysofWeek[1:-1]:
	print(days)

# //*********************************************************

# Section 4

print(f'\nSection 4: Stack')

stack = [10, 24, 31, 45, 19, 76]
len_stack = len(stack)
print(f'There are {len_stack} items on the stack')

for _ in range(3):
	stack.pop()
short_stack = len(stack)
print(f'There are {short_stack} items on the stack')

print(f'The next item on the stack is: {stack[-1]}')

# //*********************************************************

# Section 5

from collections import deque

print(f'\nSection: 5 Queue')
queue = [10, 24, 31, 45, 19, 76]

len_queue = len(queue)
print(f'There are {len_queue} items on the queue')

my_queue = deque(queue)
for i in range(3):
	my_queue.popleft()
count_queue = len(my_queue)
print(f'There are {count_queue} items on the queue')
print(f'The next item on the queue is: {my_queue[0]}')

# //*********************************************************
