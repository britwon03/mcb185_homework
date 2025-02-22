import random
import sys

# Read command-line arguments
trials = int(sys.argv[1])  # Number of trials
days = int(sys.argv[2])  # Number of days in a year
people = int(sys.argv[3])  # Number of people in the room

shared = 0  

for t in range(trials): 
    peeps = []  # Empty list of students
    for i in range(people):  # Adding 'people' students to list 
        bday = random.randint(0, days - 1)  # Generate birthday within range
        if bday in peeps:  # Check for duplicates
            shared += 1 
            break  # Stop checking if a shared birthday is found
        else: 
            peeps.append(bday)  # Add birthday to the list

print(shared / trials)  # Probability of at least one shared birthday




