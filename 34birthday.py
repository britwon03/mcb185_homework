import random
import sys

# Read command-line arguments
trials = int(sys.argv[1])  # Number of trials
days = int(sys.argv[2])  # Number of days in a year
people = int(sys.argv[3])  # Number of people in the room

shared = 0  

for t in range(trials):
    calendar = [0] * days  # Initialize a list representing all days
    for i in range(people):  # Assign birthdays to 'people' students
        bday = random.randint(0, days - 1)
        calendar[bday] += 1  # Mark the assigned birthday
        if calendar[bday] > 1:  # If a birthday is assigned more than once, it's shared
            shared += 1
            break  # Stop checking for this trial

print(shared / trials)  # Probability of at least one shared birthday
