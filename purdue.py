# Define the list of courses
courses = ['IT513: Research and Writing for the IT Professional', 'IT510: Systems Analysis Design']
 
# Loop through each week
for week in range(1, 11):
    print(f"Week {week}\n")
    for course in courses:
        print(f'{course}\n')
        print('Seminar\n'
              'Reading\n'
              'Assignment\n'
              'Discussion 1\n'
              'Discussion 2\n'
              'Discussion 3\n')
        print()  # Add a blank line for better readability
    print()  # Add a blank line to separate weeks
